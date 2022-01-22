class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String,Integer> map = new HashMap<>();
        for(String domains : cpdomains){
            int count = Integer.parseInt(domains.split(" ")[0]);
            String domain = domains.split(" ")[1];
            String[] parts = domain.split("\\.");
            int k = 0;
            for(int i=0;i<parts.length;i++){
                String part = domain.substring(k);
                k = k + parts[i].length() + 1;
                map.put(part,map.getOrDefault(part,0)+count);
            }
        }
        List<String> resultList = new ArrayList<>();
        for(Map.Entry<String,Integer> entry : map.entrySet()){
            String str = entry.getValue() + " " + entry.getKey();
            resultList.add(str);
        }
        return resultList;
    }
}