class Solution {
    public int numTilePossibilities(String tiles) {
        Set<String> set=new HashSet<>();
        numTilePossibilities(tiles,set,"");
        return set.size();
    }
    
    public void numTilePossibilities(String tiles,Set<String> set,String target){
        if(target.length()>0){
            set.add(target);
        }
        if(tiles.equals("")){
            return;
        }
        for(int i=0;i<tiles.length();i++){
            numTilePossibilities(tiles.substring(0,i)+tiles.substring(i+1),set,target+tiles.charAt(i));
        }
    }
}