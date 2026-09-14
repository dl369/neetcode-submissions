class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int numIslands = 0;
        int m = grid.size();
        int n = grid[0].size();

        auto dfs = [&](this auto& self, int r, int c) -> void {
            if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == '0') {
                return;
            }

            grid[r][c] = '0';
            self(r + 1, c);
            self(r - 1, c);
            self(r, c + 1);
            self(r, c - 1);

            return;
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    ++numIslands;
                    dfs(i, j);
                }
            }
        }

        return numIslands;
    }
};
