<template>
  <div>
    <h1 class="title has-text-centered">GPIO</h1>
    <GPIO />
  </div>
</template>

<script>
  import GPIO from "./GPIO"

  export default {
    name: "GPIOComponent",
    components: { GPIO },
  }
</script>
