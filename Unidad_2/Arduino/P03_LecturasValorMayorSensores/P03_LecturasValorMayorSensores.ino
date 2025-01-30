//PROPROCESAMIENTO DE DATOS...
//
//NORMALMENTE LEEMOS UNICAMENTE UNA VEZ CADA SENSOR Y MANDAMOS 
//LA INFORMACION AL PUERTO SERIAL...
//
//ESTO ES INCORRECTO DEBIDO A QUE PODRIAN GENERARSE 
// INCONSISTENCIAS EN LAS LECTURAS, POR LO QUE DEBE BUSCARSE
// TRATAR DE AMINORAR ESTA SITUACION MEDIANTE EL PREPROCESAMIENTO...
//
// PRIMERA APROXIMACION.... MEDIDAS DE TENDENCIA CENTRAL...>.<!
//
int sensor = A0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
//Valor Mayor
int totLecturas = 30; 
int valor[30]; //vector 
int valorMayor = -1; //
void loop() {
  // put your main code here, to run repeatedly:
  for(int i = 0; i<totLecturas;i++){
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }
  valorMayor = -1;
  for(int i = 0; i<totLecturas;i++){
    if(valor[i]>valorMayor){
      valorMayor = valor[i];
    }
  }  

  Serial.println(valorMayor);

  delay(10);
}
