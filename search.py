#!/usr/bin/env python3

import argparse
from datetime import date, datetime, timedelta
import sys

from core.api import Api

parser = argparse.ArgumentParser(description='Busca citas')
parser.add_argument(
    '--categoria', help="Categoría (por defecto 'Padrón y censo')", type=int, default=162)
parser.add_argument(
    '--familia', help="Familia (por defecto 'Altas, bajas y cambio de domicilio en Padrón')", type=int, default=321)
parser.add_argument(
    '--servicio', help="Servicio (por defecto 'Gestiones Padrón municipal')", type=int, default=22)
parser.add_argument(
    '--dias', help='Intervalo de días a partir de hoy (por defecto 60), o día máximo en formato MM.DD', type=float, default=60)

args = parser.parse_args()
if int(args.dias) == args.dias:
    args.dias = int(args.dias)
else:
    mes = int(args.dias)
    dia = int(args.dias*100)-(mes*100)
    hoy = date.today()
    dia = date(hoy.year, mes, dia)
    args.dias = (dia - hoy).days
    if args.dias<=0:
        sys.exit("No se puede buscar en el pasado")


def drange(ini, fin):
    now = datetime.now()
    for d in range(ini, fin):
        yield (now + timedelta(days=d)).date()


WKD = 'LMXJVSD'
api = Api()

ser = api.get_categoria(
    args.categoria, familia=args.familia, servicio=args.servicio)
for d in drange(1, args.dias):
    huecos = {}
    for o in ser.oficinas:
        for t in o.tramites:
            if (t.idFamiliaCita, t.idTipoServicio) != (args.familia, args.servicio):
                continue
            for h in set(map(lambda x: x.split(":")[0], api.get_huecos(t.idTramite, d))):
                ih = int(h)
                if d > date(2023, 1, 9) and int(h) < 15:
                    continue
                if h not in huecos:
                    huecos[h] = []
                huecos[h].append(o)
    if len(huecos):
        print(WKD[d.weekday()], d.strftime("%Y-%m-%d"))
        for h, os in sorted(huecos.items(), key=lambda x: x[0]):
            print(" ", h, os[0].nombreOficina, os[0].direccion)
            for o in os[1:]:
                print("    ", o.nombreOficina, o.direccion)
