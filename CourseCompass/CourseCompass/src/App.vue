<template>
  <div class="app">
    <div class="background"></div>
    <nav class="navbar">
      <div class="nav-left">
        <router-link to="/home" class="logo">Hammer</router-link>
        
        <div class="dropdown">
          <button class="dropbtn">Catalog</button>
          <div class="dropdown-content">
            <router-link to="/catalog">Catalog</router-link>
          </div>
        </div>
         
        <div class="dropdown">
          <button class="dropbtn">Tasks</button>
          <div class="dropdown-content">
            <router-link to="/to-do">To-Do</router-link>
            <router-link to="/complete">Complete</router-link>
          </div>
        </div>
      </div>
      
      <div class="profile-container" @click="toggleDropdown">
        <div class="profile-icon">
          <img src="@/assets/profile_image.jpg" alt="Profile" style="width:60px;height:60px;">
        </div>
        <div v-if="showDropdown" class="profile-dropdown">
          <router-link to="/profile">Profile</router-link>
          <router-link to="/settings">Settings</router-link>
          <router-link to="/login">Logout</router-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showDropdown: false,
    };
  },
  methods: {
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    },
  },
};
</script>

<style scoped>
@import '@/assets/styles.css';
</style>
