
import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {


    static int n, m;
    static int[][] map;
    static boolean[][] visit;
    static int count = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //   StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
         n = Integer.parseInt(st.nextToken());
         m = Integer.parseInt(st.nextToken());

        visit = new boolean[n][m];
        map = new int[n][m];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = s.charAt(j) - '0';

            }

        }
        bfs();
        System.out.println(map[n-1][m-1]);


    }

    static void bfs() {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};


        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();

        q1.offer(0);
        q2.offer(0);

        visit[0][0] = true;

        while (!q1.isEmpty()) {
            int i = q1.poll();
            int j = q2.poll();

            for (int a = 0; a < 4; a++) {
                int nr = i + dx[a];
                int nc = j + dy[a];


                if (nr >= 0 && nc >= 0 && nr < n && nc < m) {

                    if (map[nr][nc] == 1 && !visit[nr][nc]) {
                        q1.add(nr);
                        q2.add(nc);

                        visit[nr][nc] = true;

                        map[nr][nc] = map[i][j] + 1;

                    }

                }

            }
        }

    }
}