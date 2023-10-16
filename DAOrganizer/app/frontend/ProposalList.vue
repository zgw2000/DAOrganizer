<template>
  <div>
    <h1>Proposal List</h1>
    <ul>
      <li v-for="proposal in proposals" :key="proposal.id">
        <router-link :to="'/proposal/' + proposal.id">{{ proposal.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      proposals: [
        { id: 1, title: 'Proposal 1', description: 'Description for Proposal 1' },
        { id: 2, title: 'Proposal 2', description: 'Description for Proposal 2' },
        // Add more proposals here
      ],
    };
  },
};
</script>

