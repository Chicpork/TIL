import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class problem5 {
    public static void main(String[] args) {
        String play_time = "99:59:59";
        String adv_time = "25:00:00";
        String[] logs = {"69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00", "12:00:00-31:00:00"};
        String answer = "";
        String[] temp = null;
        int i_adv_time = getTimeBySecond(adv_time);
        int i_end_time = getTimeBySecond(play_time);
        int start = 0, end = 0;
        int[][] watchTime = new int[logs.length][2];
        HashMap<Integer, Integer> watched = new HashMap<>();
        for (int i = 0; i < logs.length; i++) {
            temp = logs[i].split("-");
            start = getTimeBySecond(temp[0]);
            end = getTimeBySecond(temp[1]);
            watchTime[i][0] = start;
            watchTime[i][1] = end;
            watched.put(start, 0);
            watched.put(end, 0);
        }

        Set<Integer> timeSet = watched.keySet();
        Integer[] times = new Integer[timeSet.size()];
        timeSet.toArray(times);
        Arrays.sort(times);

        for (int j = 0; j < watchTime.length; j++) {
            for (int i = 0; i < times.length; i++) {
                if (watchTime[j][0] <= times[i] && watchTime[j][1] > times[i]) {
                    watched.put(times[i], (watched.get(times[i]) + 1));
                }
                if (watchTime[j][1] <= times[i]) {
                    break;
                }
            }
        }
        for (Integer integer : times) {
            System.out.println(getSecondTimeTohhmmss(integer) + "=" + watched.get(integer) + " ");
        }

        int startTime = 0, endTime = 0, lapsTime = 0;
        int maxMoment = -1, maxMoment2 = -1;
        int maxLapsTime = -1, maxLapsTime2 = -1;

        for (int i = times.length-1; i >= 0; i--) {
            lapsTime = 0;
            startTime = getStartTime(times[i], i_adv_time);

            for (int j = i; j >= 1; j--) {
                if (startTime <= times[j-1]) {
                    if (j == 1) {
                        lapsTime = lapsTime + (times[j] - startTime) * watched.get(times[j-1]);
                    } else {
                        lapsTime = lapsTime + (times[j] - times[j-1]) * watched.get(times[j-1]);
                    }
                } else {
                    lapsTime = lapsTime + (times[j] - startTime) * watched.get(times[j-1]);
                    break;
                }
            }

            if (lapsTime >= maxLapsTime) {
                maxLapsTime = lapsTime;
                maxMoment = startTime;
            }
        }

        for (int i = 0; i < times.length; i++) {
            lapsTime = 0;
            endTime = getEndTime(times[i], i_end_time, i_adv_time);;
            for (int j = i; j < times.length-1; j++) {
                if (endTime >= times[j+1]) {
                    if (j == times.length-1) {
                        lapsTime = lapsTime + (endTime - times[j]) * watched.get(times[j]);
                    } else {
                        lapsTime = lapsTime + (times[j+1] - times[j]) * watched.get(times[j]);
                    }
                } else {
                    lapsTime = lapsTime + (endTime - times[j]) * watched.get(times[j]);
                    break;
                }
            }
            if (lapsTime > maxLapsTime2) {
                maxLapsTime2 = lapsTime;
                maxMoment2 = times[i];
            }
        }

        if( maxLapsTime == maxLapsTime2) {
            answer = getSecondTimeTohhmmss(maxMoment > maxMoment2 ? maxMoment2 : maxMoment);
        } else {
            answer = maxLapsTime > maxLapsTime2 ? getSecondTimeTohhmmss(maxMoment) : getSecondTimeTohhmmss(maxMoment2);
        }
    }

    public static int getStartTime(int endTime, int addtime) {
        return endTime - addtime < 0 ? 0 : endTime -addtime;
    }

    public static int getEndTime(int startTime, int endTime, int addtime) {
        return startTime + addtime > endTime ? endTime : startTime + addtime;
    }

    public static String getSecondTimeTohhmmss(int second) {
        return String.format("%02d:%02d:%02d", second/(60*60), (second/(60))%60, second%60);
    }

    public static int getTimeBySecond(String time) {
        String[] times  = time.split(":");
        return Integer.parseInt(times[0])*3600 + Integer.parseInt(times[1])*60 + Integer.parseInt(times[2]);
    }
}
