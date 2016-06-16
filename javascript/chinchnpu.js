var eleccion1 = prompt("Jugador 1 escoge tu movimiento");

if (eleccion1 == 'piedra') {
  eleccion1 = -2;
}
else if (eleccion1 == 'papel') {
  eleccion1 = 0;
}
else if (eleccion1 == 'tijeras') {
  eleccion1 = 1;
}
else {
  console.log("Solo puedes escoger: piedra, papel o tijeras");
}

var eleccion2 = prompt("Jugador 2 escoge tu movimiento");

if (eleccion2 == 'piedra') {
  eleccion2 = -2;
}
else if (eleccion2 == 'papel') {
  eleccion2 = 0;
}
else if (eleccion2 == 'tijeras') {
  eleccion2 = 1;
}
else {
  console.log("Solo puedes escoger: piedra, papel o tijeras");
}

switch (eleccion1, eleccion2) {
  case eleccion1==eleccion2:
    console.log("Empate");
    break;
  case eleccion1 && eleccion2 !== 0:
  case eleccion1 == -2:
    console.log("Gana el jugador 1, piedra aplasta tijeras");
    break;
  case eleccion2 == -2:
    console.log("Gana el jugador 2, piedra aplasta tijeras");
    break;
  case eleccion1 && eleccion2 !== 1:
  case eleccion1 == 0:
    console.log("Gana el jugador 1, papel enrolla piedra");
    break;
  case eleccion2 == 0:
    console.log("Gana el jugador 2, papel enrolla piedra");
    break;
  case eleccion1 > eleccion2:
    console.log("Jugador 1 gana, tijeras cortan papel");
    break;
    case eleccion1 < eleccion2:
      console.log("Jugador 2 gana, tijeras cortan papel");
      break;
  default:
  console.log("Error");
    break;
}
