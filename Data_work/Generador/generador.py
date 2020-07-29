# -*- coding: utf-8 -*-

import re
from experta import *

class Producto(Fact):
    """
    Producto que ha comprado el cliente.
    >>> Producto(nombre="pepsi", tipo="refresco de cola", cantidad=1)
    """
    pass

class Cupon(Fact):
    """
    Cupon a generar para la proxima compra del cliente.
    >>> Cupon(tipo="2x1", producto="pepsi")
    """
    pass

class Promo(Fact):
    """
    Promocion vigente en el comercio.
    >>> Promo(tipo="2x1", **depende_de_la_promo)
    """
    pass

class Beneficio(Fact):
    """
    Define los beneficios que obtiene el comercio por cada producto.
    >>> Beneficio(nombre="pepsi", tipo="refresco de cola", ganancias=0.2)
    """
    pass

class OfertasNxM(KnowledgeEngine):
    @DefFacts()
    def carga_promociones_nxm(self):
        """
        Hechos iniciales.
        Genera las promociones vigentes
        """
        # yield Promo(tipo="2x1", producto="Dodot")
        # yield Promo(tipo="2x1", producto="Leche Pascual")
        # yield Promo(tipo="3x2", producto="Pilas AAA")
        # yield Promo(tipo="2x1", producto="Dodot")
        # yield Promo(tipo="2x1", producto="Leche Pascual")
        # yield Promo(tipo="3x2", producto="Pilas AAA")
        for i in range(1,5):
            yield Promo(tipo="3x2", producto=str(i*10))
            yield Promo(tipo="2x1", producto=str(i*11))
          
            

            
    @Rule(Promo(tipo=MATCH.t & P(lambda t: re.match(r"\d+x\d+", t)),producto=MATCH.p),Producto(nombre=MATCH.p))
    
    def oferta_nxm(self, t,p):
        """
        Sabemos que el cliente volvera aprovechar 
        la promocion, ya que hoy ha comprado el producto.
        """
        self.declare(Cupon(tipo=t, producto=p))




watch('RULES', 'FACTS')
nxm = OfertasNxM()
nxm.reset()
# nxm.declare(Producto(nombre="Dodot"))
# nxm.declare(Producto(nombre="Agua Mineral"))
# nxm.declare(Producto(nombre="Pilas AAA"))

nxm.declare(Producto(nombre="10"))
nxm.declare(Producto(nombre="33"))

nxm.run()
        
      
class OfertasPACK(KnowledgeEngine):
    @DefFacts()
    def carga_promociones_pack(self):
        """Genera las promociones vigentes"""
        for i in range(1,5):
            yield Promo(tipo="PACK", producto1=str(i*10), producto2=str(i*5), descuento="25%")
            yield Promo(tipo="PACK", producto1=str(i*11), producto2=str(i), descuento="10%")

    @Rule(Promo(tipo="PACK", producto1=MATCH.p1, producto2=MATCH.p2, descuento=MATCH.d),
          OR(
              AND(
                  NOT(Producto(nombre=MATCH.p1)),
                  Producto(nombre=MATCH.p2)
              ),
              AND(
                  Producto(nombre=MATCH.p1),
                  NOT(Producto(nombre=MATCH.p2))
              )
          )
    )
    def pack(self, p1, p2, d):
        """
        El cliente querrá comprar un producto adicional en su próxima visita.
        """
        self.declare(Cupon(tipo="PACK", producto1=p1, producto2=p2, descuento=d))

pack = OfertasPACK()
pack.reset()
pack.declare(Producto(nombre="15"))
pack.declare(Producto(nombre="11"))
pack.run()



facts = pack.facts
#print(facts)
datos=[]

for fact in facts.values():
    #print(fact.values())
    if isinstance(fact,Cupon):
        producto1=fact['producto1']
        producto2=fact['producto2']
        tipo=fact['tipo']
        descuento=fact['descuento']
        print(producto1, producto2,tipo,descuento)
        resultado={'producto1':producto1, 'producto2':producto2, 'tipo':tipo,'descuento':descuento}
        datos.append(resultado)
        
print(datos)



















    