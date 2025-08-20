import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int M;
    static int start;
    static int[][] arr;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();
    static Queue<Integer> q = new LinkedList<>();

    public static void dfs(int x){
        visited[x] = true;
        sb.append(x + " ");

        for (int i = 1; i <= N; i++){
            if(arr[x][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int x){
        q.offer(x);
        visited[x] = true;

        while(!q.isEmpty()){
            int cur = q.poll();
            sb.append(cur + " ");

            for (int i = 1; i <= N; i++){
                if(arr[cur][i] == 1 && !visited[i]){
                    q.offer(i);
                    visited[i] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());   // 노드
        M = Integer.parseInt(st.nextToken());   // 간선
        start = Integer.parseInt(st.nextToken());

        arr = new int[N+1][N+1];
        visited = new boolean[N+1];

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a][b] = arr[b][a] = 1;   // 인접행렬
        }

        dfs(start);
        sb.append('\n');
        visited = new boolean[N+1];
        bfs(start);

        System.out.println(sb);
    }
}
