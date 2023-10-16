<script setup>
defineProps({
    data: Number,
    title: String,
    description: String,
    title_gradient: String 
})
</script>

<template>
    <article >
        <h1 :class=title_gradient>{{data}}</h1>
        <h2>{{title}}</h2>
        <p>{{description}}</p>
    </article>   
</template>



<style scoped>
article {
  display: flex;
  width: 30%;
  padding: 50px 28px;
  flex-direction: column;
  justify-content: center;
  align-items: center; 

  border-radius: 20px;
  background-color: #FFF;
  box-shadow: 0px 4px 15px 0px rgba(0, 0, 0, 0.05);

  text-align: center;
  font-style: normal;
}
h1{
  font-size: 80px;
  font-weight: 600;
  line-height: 91px; 

  color: black;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

h2{
  color: #1B1B1B;
  font-size: 26px;
  font-weight: 600;
  line-height: 54px; 
}

p{
  font-size: 18px;
  font-weight: 500;
  line-height: 21px; 
  color: #4A5568; 
}

.purple  {
  background-image: var(--GradienteRoxo)
}
.green{
  background-image: var(--GradientVerde); 
}
.red{
  background-image: var(--GradientVermelho);
}
</style>