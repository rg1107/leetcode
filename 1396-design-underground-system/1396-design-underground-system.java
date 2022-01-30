class UndergroundSystem {

    private Map<Integer, OnGoingTrip> onGoingTripMap;
    private Map<String, List<Integer>> finishedTripDurationMap;

    public UndergroundSystem() {
        this.onGoingTripMap = new HashMap<>();
        this.finishedTripDurationMap = new HashMap<>();
    }

    public void checkIn(int id, String stationName, int t) {
        var onGoingTrip = new OnGoingTrip(stationName, t);
        onGoingTripMap.put(id, onGoingTrip);
    }

    public void checkOut(int id, String stationName, int t) {
        var onGoingTrip = onGoingTripMap.get(id);
        var tripDuration = t - onGoingTrip.getTripStartTime();
        var stationToStationKey = stationToStationKey(onGoingTrip.getSource(), stationName);
        if (!finishedTripDurationMap.containsKey(stationToStationKey))
            finishedTripDurationMap.put(stationToStationKey, new ArrayList<>() {{
                add(tripDuration);
            }});
        else
            finishedTripDurationMap.get(stationToStationKey).add(tripDuration);
        onGoingTripMap.remove(id);
    }

    public double getAverageTime(String startStation, String endStation) {
        var key = stationToStationKey(startStation, endStation);
        var travelsDuration = finishedTripDurationMap.get(key);
        return travelsDuration.stream().mapToDouble(d -> (double) d).average().orElse(-1);
    }
    
    private String stationToStationKey(String firstStation, String secondStation) {
        return firstStation + "-" + secondStation;
    }

    private class OnGoingTrip {
        private final String source;
        private final int tripStartTime;

        public OnGoingTrip(String source, int start) {
            this.source = source;
            this.tripStartTime = start;
        }

        public String getSource() {
            return source;
        }

        public int getTripStartTime() {
            return tripStartTime;
        }
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */