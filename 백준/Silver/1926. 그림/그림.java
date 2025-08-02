import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class Main {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static int n, m;
    static int[][] arr;
    static boolean[][] visited;
//    static int[][] arr_1;
    static int maxArea = 0;

    static int bfs(int x, int y) {
//        StringBuilder sb = new StringBuilder();
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visited[x][y] = true;
        int area = 1;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (arr[nx][ny] == 0 || visited[nx][ny]) continue;
//                if () continue;

                visited[nx][ny] = true;   //방문 처리 및 거리 갱신
                q.offer(new int[]{nx, ny});
                area++;

            }
        }
        return area;

    }
        public static void main (String[]args){
            Scanner sc = new Scanner(System.in);
            int cnt = 0;
            n = sc.nextInt();
            m = sc.nextInt();

            arr = new int[n][m];
            visited = new boolean[n][m];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    arr[i][j] = sc.nextInt();
                }
            }

//            System.out.println("입력된 배열:");
//            for (int i = 0; i < n; i++) {
//                System.out.println(Arrays.toString(arr[i]));
//            }

            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++){
                    if(arr[i][j] ==1 && !visited[i][j]){
                        int area = bfs(i, j);
                        cnt++;
                        maxArea = Math.max(maxArea, area);

                    }
                }
            }
            System.out.println(cnt);
            System.out.println(maxArea);

        }
}
