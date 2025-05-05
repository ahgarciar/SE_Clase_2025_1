const express = require('express')

const controller = require('../../controllers/devicesController')

//RUTAS
const router = express.Router()

// /api/v1-actuators/actuators
router
   // http://localhost:3000/api/v1/  ->> volley
                                  // --> http
  .get("/", controller.getAll_records) 
  
  // http://localhost:3000/api/v1/optimizar/X
  .get("/optimizar/:idDevice", controller.getLast_Record)

  // http://localhost:3000/api/v1-actuators/actuators/2
  .get("/decision", controller.getLastDecision) 
  
  //INSERT NEW RECORD
  // http://localhost:3000/api/v1-actuators/actuators/
  .post("/registros", controller.insertRecord) 
  
  //INSERT DECISION
  // http://localhost:3000/api/v1-actuators/actuators/
  .post("/decision", controller.insertDecision) 

  //EXPORTA EL ROUTER PARA HACER POSIBLE SU POSTERIOR IMPORTANCION Y USO EN OTROS MODULOS
module.exports = router;