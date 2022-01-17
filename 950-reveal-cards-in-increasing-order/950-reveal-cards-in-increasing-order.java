class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        ArrayDeque<Integer> q=new ArrayDeque();
        int i=deck.length-1;
        Arrays.sort(deck);
        while(q.size()!=deck.length){
            if(i==0){
                q.offerFirst(deck[i]);break;
            }
            q.offerFirst(deck[i--]);
            q.offerFirst(q.pollLast());
        }
        int j=0;
        for(int k:q){
            deck[j++]=k;
        }
        return deck;
        
    }
}