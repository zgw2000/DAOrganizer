use ink_lang as ink;

#[ink::contract]
mod dao_organizer {
    use ink_prelude::vec::Vec;
    use ink_storage::collections::{HashMap as StorageHashMap, Vec as StorageVec};
    use ink_storage::traits::{PackedLayout, SpreadLayout};
    
    #[derive(Debug, Clone, PartialEq, Eq, scale::Encode, scale::Decode, SpreadLayout, PackedLayout)]
    #[cfg_attr(feature = "std", derive(scale_info::TypeInfo, ink_storage::traits::StorageLayout))]
    pub struct Proposal {
        title: String,
        description: String,
        votes: u32,
    }
    
    #[ink(storage)]
    pub struct DAOrganizer {
        owner: AccountId,
        proposals: StorageHashMap<ProposalId, Proposal>,
        voters: StorageHashMap<AccountId, bool>,
        proposal_ids: StorageVec<ProposalId>,
    }
    
    #[ink(event)]
    pub struct ProposalCreated {
        #[ink(topic)]
        id: ProposalId,
        title: String,
    }
    
    #[ink(event)]
    pub struct Voted {
        #[ink(topic)]
        proposal_id: ProposalId,
        voter: AccountId,
    }
    
    #[ink(impl)]
    impl DAOrganizer {
        #[ink(constructor)]
        pub fn new() -> Self {
            let caller = Self::env().caller();
            Self {
                owner: caller,
                proposals: Default::default(),
                voters: Default::default(),
                proposal_ids: Default::default(),
            }
        }
        
        #[ink(message)]
        pub fn create_proposal(&mut self, title: String, description: String) -> ProposalId {
            let caller = self.env().caller();
            assert_eq!(caller, self.owner, "Only the owner can create proposals");
            
            let proposal_id = self.next_proposal_id();
            let proposal = Proposal {
                title: title.clone(),
                description,
                votes: 0,
            };
            self.proposals.insert(proposal_id, proposal);
            self.proposal_ids.push(proposal_id);
            
            self.env().emit_event(ProposalCreated {
                id: proposal_id,
                title,
            });
            
            proposal_id
        }
        
        #[ink(message)]
        pub fn vote(&mut self, proposal_id: ProposalId) {
            let caller = self.env().caller();
            assert!(!self.voters.contains_key(&caller), "You have already voted");
            
            let mut proposal = self.proposals.get_mut(&proposal_id).unwrap();
            proposal.votes += 1;
            
            self.voters.insert(caller, true);
            
            self.env().emit_event(Voted {
                proposal_id,
                voter: caller,
            });
        }
        
        #[ink(message)]
        pub fn get_proposal(&self, proposal_id: ProposalId) -> Option<&Proposal> {
            self.proposals.get(&proposal_id)
        }
        
        #[ink(message)]
        pub fn get_proposals(&self) -> Vec<ProposalId> {
            self.proposal_ids.clone()
        }
        
        fn next_proposal_id(&self) -> ProposalId {
            let current_proposal_count = self.proposal_ids.len() as u32;
            current_proposal_count + 1
        }
    }
}
