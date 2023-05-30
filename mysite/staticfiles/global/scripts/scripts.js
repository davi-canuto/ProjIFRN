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