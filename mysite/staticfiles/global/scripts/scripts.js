// Obtém a referência para o botão de filtro
var filterButton = document.querySelector('.filter-btn');

// Obtém a referência para o elemento de filtro
var filters = document.getElementById('filters');

// Adiciona um ouvinte de evento ao botão de filtro
filterButton.addEventListener('click', function(event) {
  // Evita que o evento de clique propague para outros elementos
  event.stopPropagation();

  // Alterna a classe "show" no elemento de filtro
  filters.classList.toggle('show');
});

// Adiciona um ouvinte de evento ao documento para fechar o dropdown ao clicar em outro lugar da tela
document.addEventListener('click', function(event) {
  // Verifica se o clique não ocorreu dentro do elemento de filtro ou do botão de filtro
  if (!filters.contains(event.target) && !filterButton.contains(event.target)) {
    // Remove a classe "show" do elemento de filtro
    filters.classList.remove('show');
  }
});

function left(){
  var element = document.querySelector('#desloc')
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

function right(len){
  var element = document.querySelector('#desloc')
  const card = document.querySelector('.card')
  
  const totalPixelsList = card.offsetWidth * len

  var currentMarginLeft = parseInt(window.getComputedStyle(element).marginLeft);
  
  var x = currentMarginLeft - Math.round(window.innerWidth / 2);

  if((window.innerWidth - totalPixelsList) > x){
    x = window.innerWidth - totalPixelsList - 30
  }

  element.style.marginLeft = x + 'px';  
  
}


function toggleDropdown() {
  var dropdownContent = document.getElementById("myDropdown");
  dropdownContent.classList.toggle("show");
}