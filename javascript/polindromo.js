var palabra = "ana";
function encuentraPalindromo(palabra) {
  lista = palabra.split();
  lista2 = lista.reverse();
  if (lista == lista2) {
    console.log("Si es un palindromo");
  }
  else {
    console.log("No es un palindormo");
  }
}
encuentraPalindromo(palabra);
