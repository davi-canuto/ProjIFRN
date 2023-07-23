function leftAnd(){
    var element = document.querySelector('#id_andamento')
    console.log(element.style.marginLeft)
  
    var currentMarginLeft = parseInt(window.getComputedStyle(element).marginLeft);
    
    var screenWidth = window.innerWidth;
    // Define a quantidade de pixels a serem acrescentados
    var additionalPixels = Math.round(screenWidth / 2);
    
    // Calcula o novo valor da margem esquerda
    var newMarginLeft = currentMarginLeft + additionalPixels;
    console.log(newMarginLeft)
    
    if(newMarginLeft > 0){
    element.style.marginLeft = 0 + 'px';
    }
    else{
      // Aplica a nova margem esquerda ao elemento
      element.style.marginLeft = newMarginLeft + 'px';  
    }
    
  }
  
  
  function leftFin(){
    var element = document.querySelector('#id_finalizado')
    console.log(element.style.marginLeft)
  
    var currentMarginLeft = parseInt(window.getComputedStyle(element).marginLeft);
    
    var screenWidth = window.innerWidth;
    // Define a quantidade de pixels a serem acrescentados
    var additionalPixels = Math.round(screenWidth / 2);
    
    // Calcula o novo valor da margem esquerda
    var newMarginLeft = currentMarginLeft + additionalPixels;
    console.log(newMarginLeft)
    
    if(newMarginLeft > 0){
    element.style.marginLeft = 0 + 'px';
    }
    else{
      // Aplica a nova margem esquerda ao elemento
      element.style.marginLeft = newMarginLeft + 'px';  
    }
    
  }
  
  function rightAnd(len){
    var element = document.querySelector('#id_andamento')
    const card = document.querySelector('.card')
    
    const totalPixelsList = card.offsetWidth * len
  
    var currentMarginLeft = parseInt(window.getComputedStyle(element).marginLeft);
    
    var x = currentMarginLeft - Math.round(window.innerWidth / 2);
  
    if((window.innerWidth - totalPixelsList) > x){
      x = window.innerWidth - totalPixelsList - 30
    }
  
    element.style.marginLeft = x + 'px';  
    
  }
  
  
  function rightFin(len){
    var element = document.querySelector('#id_finalizado')
    const card = document.querySelector('.card')
    
    const totalPixelsList = card.offsetWidth * len
  
    var currentMarginLeft = parseInt(window.getComputedStyle(element).marginLeft);
    
    var x = currentMarginLeft - Math.round(window.innerWidth / 2);
  
    if((window.innerWidth - totalPixelsList) > x){
      x = window.innerWidth - totalPixelsList - 30
    }
  
    element.style.marginLeft = x + 'px';  
    
  }