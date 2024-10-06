import typer
from funcoes.linear import funcao_linear
from funcoes.quadratica import funcao_quadratica
from funcoes.polinomial_de_grau_3 import funcao_polinomial
from funcoes.modular import funcao_modular
from funcoes.exponencial import funcao_exponencial
from funcoes.logaritmica import funcao_logaritmica

app = typer.Typer()

@app.command()
def linear(a: float = typer.Option(...), b: float = typer.Option(...)):       
    try:        
        funcao_linear(a, b)
    except Exception as e:
        print(e)
        
@app.command()
def quadratica(a: float = typer.Option(...), b: float = typer.Option(...), c: float = typer.Option(...)):       
    try:        
      funcao_quadratica(a, b, c)
    except Exception as e:
        print(e)
        
@app.command()
def polinomial(a: float = typer.Option(...), b: float = typer.Option(...), c: float = typer.Option(...), d: float = typer.Option(...)):       
    try:        
      funcao_polinomial(a, b, c, d)
    except Exception as e:
        print(e)
        
@app.command()
def modular(x: float = typer.Option(...)):       
    try:        
      funcao_modular(x)
    except Exception as e:
        print(e)
        
@app.command()
def exponencial(a: float = typer.Option(...), b: float = typer.Option(...)):       
    try:        
      funcao_exponencial(a, b)
    except Exception as e:
        print(e)
      
@app.command()
def logaritmica(a: float = typer.Option(...)):       
    try:        
      funcao_logaritmica(a)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app()