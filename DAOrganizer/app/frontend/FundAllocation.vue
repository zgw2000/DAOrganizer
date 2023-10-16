<template>
  <div>
    <h1>Fund Allocation</h1>
    <p>Total Funds: {{ totalFunds }}</p>
    
    <div v-for="(proposal, index) in proposals" :key="index">
      <h2>{{ proposal.title }}</h2>
      <p>{{ proposal.description }}</p>
      <input type="number" v-model="proposal.allocation" :min="0" :max="totalFunds">
      <button @click="allocateFunds(proposal)">Allocate</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      totalFunds: 10000, // Example total funds
      proposals: [
        { id: 1, title: 'Proposal 1', description: 'Description for Proposal 1', allocation: 0 },
        { id: 2, title: 'Proposal 2', description: 'Description for Proposal 2', allocation: 0 },
        // Add more proposals here
      ],
    };
  },
  methods: {
    allocateFunds(proposal) {
      // Implement the logic to allocate funds to a proposal and update the 'allocation' field
    },
  },
};
</script>
