function fileOpen(){
    var input = document.createElement("input");
    input.type = 'file';
    input.accept = 'text/plain'
    input.onchange = function (event){
      processFile(event.target.files[0]); //열린 파일
    };
    input.click();
  }
  
  function processFile(file){
    var reader = new FileReader();
    reader.onload = function(){
      console.log(reader.result); //필요한 곳에 사용
    };
    reader.readAsText(file,"euc-kr");
  }
  
  const fs = require("fs");
  const csv = require("csvtojson");
  const { Parser } = require('json2csv');
  
  (async () =>{
  
    //load 
    const patch = await csv().fromFile("clustered_cctv_coor.csv");
  
    console.log(coors);
  
    const coor = new Parser({fields: {
      latlng: new kako.maps.Latlng("latitude","longitude")
    }}).parse(coors);
    //fs.writeFileSync("cars.csv",)
  })