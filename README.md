# UrlApexDecode
Código simple para decodificar una url de apex

### Uso
Para usarlo simplente llamaelo e ingrese la url cuabdo se lo solicite o envie la url como primer argumeto

### Ejemplo
``` python
python apexdecode http://apex.somewhere.com/pls/apex/f?p=4350:1:220883407765693447:::1:P1_PAGEID,P1_IDUSER,P1_AGE:22,834573343,29:
```
Salida
Formato de una url en Apex:
f?p=App:Page:Session:Request:Debug:ClearCache:itemNames:itemValues:PrinterFriendly

Ingrese la url Apex:
Url ingresada: http://apex.somewhere.com/pls/apex/f?p=4350:1:220883407765693447:::1:P1_PAGEID,P1_IDUSER,P1_AGE:22,834573343,29:

+-------------------+----------------------------+
| Identificadores   | Valores                    |
|-------------------+----------------------------|
| App               | 4350                       |
| Page              | 1                          |
| Session           | 220883407765693447         |
| Request           |                            |
| Debug             |                            |
| ClearCache        | 1                          |
| itemNames         | P1_PAGEID,P1_IDUSER,P1_AGE |
| itemValues        | 22,834573343,29            |
| PrinterFriendly   |                            |
+-------------------+----------------------------+

+-------------+--------------+
| itemNames   |   itemValues |
|-------------+--------------|
| P1_PAGEID   |           22 |
| P1_IDUSER   |    834573343 |
| P1_AGE      |           29 |
+-------------+--------------+
