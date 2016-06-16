var lista;
lista = [0,1,1,2,3];
function fibonacci(n) {
  console.log(lista[lista.lenght-1]);
  for (var i = 0; i <= n; i++) {
  lista.push(lista[lista.lenght-2] + lista[lista.lenght-1]);
  }
  console.log(lista);
  for (var element in lista) {
    console.log(element);
  }
}
fibonacci(10);
