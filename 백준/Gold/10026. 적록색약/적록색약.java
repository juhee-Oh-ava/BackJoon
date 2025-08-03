import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;


public class Main{

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static char[][] board;
    static boolean[][] visited;
    static Queue<int[]> q = new LinkedList<>();
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        n = Integer.parseInt(br.readLine());
        board = new char[n][n];
        visited = new boolean[n][n];

        for(int i = 0; i < n; i++){
            String st = br.readLine();
            for(int j = 0; j < n; j++){
                board[i][j] = st.charAt(j);
            }
        }
        //정상인
        int cnt = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(!visited[i][j]){
                    cnt++;
                    bfs(i, j);
                }
            }
        }

        sb.append(cnt + " ");
        //색약인
        cnt = 0;
        visited = new boolean[n][n];
        for(int i = 0; i < n; i++){
            for(int j= 0; j < n; j++){
                if(!visited[i][j]){
                    cnt++;
                    bfs(i, j);
                }
            }
        }
        sb.append(cnt);
        System.out.println(sb);


    }

    public static void bfs(int x, int y){
        q.offer(new int[]{x, y});
        visited[x][y] = true;
        while(!q.isEmpty()){
            int[] t = q.poll();
            int cx = t[0];
            int cy = t[1];

            for(int i = 0; i < 4; i++){
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if(nx < 0 || ny < 0 || nx >= n || ny >= n) continue;
                //현재 칸과 다음 이동할 좌표 칸의 색이 다르면 연결된 구역이 아니므로 건너뛴다.
                if(visited[nx][ny] || board[cx][cy] != board[nx][ny]) continue;
                visited[nx][ny] = true;
                q.offer(new int[]{nx, ny});
            }
            if(board[cx][cy] == 'G')
                board[cx][cy] = 'R';
        }
    }
}