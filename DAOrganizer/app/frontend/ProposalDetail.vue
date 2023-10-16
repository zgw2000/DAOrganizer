<template>
  <div>
    <h1>Proposal Details</h1>
    <h2>{{ proposal.title }}</h2>
    <p>{{ proposal.description }}</p>
    
    <div v-if="!proposal.voted">
      <button @click="voteForProposal">Vote</button>
    </div>
    <div v-else>
      <p>You have already voted for this proposal.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      proposal: { id: 1, title: 'Proposal 1', description: 'Description for Proposal 1', voted: false },
      // Load proposal data from the backend API
    };
  },
  methods: {
    voteForProposal() {
      // Implement the logic to vote for the proposal
      // Update the 'voted' status once the vote is cast
      this.proposal.voted = true;
    },
  },
};
</script>
