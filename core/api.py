from datetime import datetime, timedelta
from time import time
from urllib.parse import urlencode

from munch import Munch

from .web import Web


class Api(Web):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.s.headers.update({
            'X-Requested-With': 'XMLHttpRequest',
            "Content-Type": "application/json"
        })
        self.root = Munch(
            categoria="https://gestionturnos.madrid.es/GNSIS_WBCIUDADANO/comboFamilias.do",
            horario="https://gestionturnos.madrid.es/GNSIS_WBCIUDADANO/franjasDia.do",
        )

    def get_json(self, *args, **kvargs):
        r = self._get(*args, **kvargs)
        try:
            j = r.json()
        except:
            print(r.url)
            raise
        return Munch.fromDict(j)

    def get_categoria(self, categoria, familia=None, servicio=None):
        url = self.root.categoria + '?' + urlencode({
            "idCategoria": categoria,
            "codTramitePrivado": ''
        }, doseq=False)
        r = self.get_json(url)
        if familia is None:
            return r
        for f in r.familiasCitas:
            if f.idFamiliaCita == familia:
                if servicio is not None:
                    for s in f.tiposServicio:
                        if s.idTipoServicio == servicio:
                            return s
                    continue
                return f
        return None

    def get_horario(self, tramite, dia):
        if isinstance(dia, int):
            dia = datetime.now() + timedelta(days=dia)
        url = self.root.horario + '?' + urlencode({
            "idTramite": tramite,
            "dia": dia.strftime("%d/%m/%Y"),
            "esUltimoDiaHuecos": "false",
            "nh": "0",
            "time": int(time()*100),
            "idTipoAtencion": "1"
        }, doseq=False)
        j = self.get_json(url)
        return j

    def get_huecos(self, *args, **kvargs):
        hs = self.get_horario(*args, **kvargs)
        huecos = set()
        for x in hs:
            for f in x.franjasMinuto:
                for h in f.huecos:
                    if h.disponible:
                        hora = str(h.hora)
                        while len(hora) < 5:
                            hora = '0'+hora
                        huecos.add(hora)
        huecos = sorted(huecos)
        return tuple(huecos)
