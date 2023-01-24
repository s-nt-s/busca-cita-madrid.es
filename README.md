Busca citas en https://gestionturnos.madrid.es/GNSIS_WBCIUDADANO/horarioTramite.do
(por defecto, citas de padrón en los próximos 60 días).

```console
$ python3 search.py --help
usage: search.py [-h] [--categoria CATEGORIA] [--familia FAMILIA]
                 [--servicio SERVICIO] [--dias DIAS]

Busca citas

optional arguments:
  -h, --help            show this help message and exit
  --categoria CATEGORIA
                        Categoría (por defecto 'Padrón y censo')
  --familia FAMILIA     Familia (por defecto 'Altas, bajas y cambio de
                        domicilio en Padrón')
  --servicio SERVICIO   Servicio (por defecto 'Gestiones Padrón municipal')
  --dias DIAS           Intervalo de días a partir de hoy (por defecto 60)
```

Formato de salida:

```
<Día> <fecha>
  <Hora redondeada> <OAC> <Dirección>
```

```
$ python3 search.py
J 2023-02-23
  15 OAC Arganzuela Paseo Chopera, 10
     OAC Barajas Plaza Mercurio, 1
     OAC Carabanchel C/ Utebo, 8
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Ciudad Lineal C/ Hermanos García Noblejas, 16
     OAC Fuencarral Av. Monforte de Lemos, 40
     OAC Hortaleza Carretera Canillas, 2
     OAC Latina Av. Las Aguilas, 2
     OAC Moratalaz C/ Fuente Carrantona, 8
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Puente Vallecas Av. Albufera, 42
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Arganzuela Paseo Chopera, 10
     OAC Barajas Plaza Mercurio, 1
     OAC Carabanchel C/ Utebo, 8
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Ciudad Lineal C/ Hermanos García Noblejas, 16
     OAC Fuencarral Av. Monforte de Lemos, 40
     OAC Hortaleza Carretera Canillas, 2
     OAC Latina Av. Las Aguilas, 2
     OAC Moratalaz C/ Fuente Carrantona, 8
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Puente Vallecas Av. Albufera, 42
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
L 2023-02-27
  15 OAC Barajas Plaza Mercurio, 1
     OAC Carabanchel C/ Utebo, 8
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Ciudad Lineal C/ Hermanos García Noblejas, 16
     OAC Fuencarral Av. Monforte de Lemos, 40
     OAC Hortaleza Carretera Canillas, 2
     OAC Latina Av. Las Aguilas, 2
     OAC Moratalaz C/ Fuente Carrantona, 8
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Puente Vallecas Av. Albufera, 42
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Barajas Plaza Mercurio, 1
     OAC Carabanchel C/ Utebo, 8
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Ciudad Lineal C/ Hermanos García Noblejas, 16
     OAC Fuencarral Av. Monforte de Lemos, 40
     OAC Hortaleza Carretera Canillas, 2
     OAC Latina Av. Las Aguilas, 2
     OAC Moratalaz C/ Fuente Carrantona, 8
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Puente Vallecas Av. Albufera, 42
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
M 2023-02-28
  15 OAC Barajas Plaza Mercurio, 1
     OAC Carabanchel C/ Utebo, 8
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Ciudad Lineal C/ Hermanos García Noblejas, 16
     OAC Fuencarral Av. Monforte de Lemos, 40
     OAC Hortaleza Carretera Canillas, 2
     OAC Latina Av. Las Aguilas, 2
     OAC Moratalaz C/ Fuente Carrantona, 8
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Puente Vallecas Av. Albufera, 42
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Barajas Plaza Mercurio, 1
     OAC Carabanchel C/ Utebo, 8
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Ciudad Lineal C/ Hermanos García Noblejas, 16
     OAC Fuencarral Av. Monforte de Lemos, 40
     OAC Hortaleza Carretera Canillas, 2
     OAC Latina Av. Las Aguilas, 2
     OAC Moratalaz C/ Fuente Carrantona, 8
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Puente Vallecas Av. Albufera, 42
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
X 2023-03-01
  15 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
J 2023-03-02
  15 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC San Blas/Canillejas Av. Arcentales, 28
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
L 2023-03-06
  15 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
M 2023-03-07
  15 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
X 2023-03-08
  15 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
J 2023-03-09
  15 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Arganzuela Paseo Chopera, 10
     OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Tetuán C/ Simancas, 6
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Vicálvaro Plaza Don Antonio de Andrés, 18
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
L 2023-03-13
  15 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
M 2023-03-14
  15 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
X 2023-03-15
  15 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
J 2023-03-16
  15 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Centro C/ Atocha, 70
     OAC Chamberí C/ Palafox, 4
     OAC Numancia [Puente de Vallecas] C/ Monte Oliveti, 14
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
M 2023-03-21
  15 OAC Chamberí C/ Palafox, 4
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Chamberí C/ Palafox, 4
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
X 2023-03-22
  15 OAC Chamberí C/ Palafox, 4
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Chamberí C/ Palafox, 4
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
J 2023-03-23
  15 OAC Chamberí C/ Palafox, 4
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
  16 OAC Chamberí C/ Palafox, 4
     OAC Sanchinarro [Hortaleza] C/ Princesa de Éboli, 29
     OAC Usera Av. Rafaela Ybarra, 41
     OAC Villa de Vallecas Paseo Federico García Lorca, 12
```