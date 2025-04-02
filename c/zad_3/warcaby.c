#include <stdio.h>
#include <stdlib.h>
#define N 20

int cnt[2];
char filler = '_';

int rnd(const int min, const int max) {
    return (rand() % (max - min)) + min;
}

void print(char board[][N], const int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%c ", board[i][j]);
        }
        printf("\n");
    }
}

void start(char board[][N], const int n){
    for (int k = 0; k < n; k++) {
        for (int l = 0; l < n; l++) {
            board[k][l] = filler;
        }
    }
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < (n/2); j++) {
            if (i%2 == 0) {
                board[i][j*2] = '1';
                board[n-1-i][j*2 + 1] = '2';
            }
            else {
                board[i][j*2 + 1] = '1';
                board[n-1-i][j*2] = '2';
            }
        }
    }

}

int move(char board[][N], const int i, const int j, const int n) {
    if (board[i][j] == '1') {
        if (i + 1 < n) {
            if (j + 1 < n && board[i+1][j+1] == filler) {
                board[i+1][j+1] = '1';
                board[i][j] = filler;
                return 1;
            }
            else if (j - 1 >= 0 && board[i+1][j-1] == filler) {
                board[i+1][j-1] = '1';
                board[i][j] = filler;
                return 1;
            }
        }
    }
    else if (board[i][j] == '2') {
        if (i - 1 >= 0) {
            if (j + 1 < n && board[i-1][j+1] == filler) {
                board[i-1][j+1] = '2';
                board[i][j] = filler;
                return 1;
            }
            else if (j - 1 >= 0 && board[i-1][j-1] == filler) {
                board[i-1][j-1] = '2';
                board[i][j] = filler;
                return 1;
            }
        }
    }
    return 0;
}

int capture(char board[][N], const int i, const int j, const int n) {
    if (board[i][j] == '1') {
        if (i + 2 < n && j + 2 < n && board[i+1][j+1] == '2' && board[i+2][j+2] == filler) {
            board[i][j] = filler;
            board[i+1][j+1] = filler;
            board[i+2][j+2] = '1';
            cnt[1]--;
            return 1;
        }
        else if (i + 2 < n && j - 2 >= 0 && board[i+1][j-1] == '2' && board[i+2][j-2] == filler) {
            board[i][j] = filler;
            board[i+1][j-1] = filler;
            board[i+2][j-2] = '1';
            cnt[1]--;
            return 1;
        }
        else {
            return 0;
        }
    }
    else if (board[i][j] == '2') {
        if (i - 2 >= 0 && j + 2 < n && board[i-1][j+1] == '1' && board[i-2][j+2] == filler) {
            board[i][j] = filler;
            board[i-1][j+1] = filler;
            board[i-2][j+2] = '2';
            cnt[0]--;
            return 1;
        }
        else if (i - 2 >= 0 && j - 2 >= 0 && board[i-1][j-1] == '1' && board[i-2][j-2] == filler) {
            board[i][j] = filler;
            board[i-1][j-1] = filler;
            board[i-2][j-2] = '2';
            cnt[0]--;
            return 1;
        }
        else{
            return 0;
        }
    }
    return 0;
}


int main(void) {
    char board[N][N];
    int n, steps;
    unsigned seed;
    scanf("%d %u %d", &n, &seed, &steps);
    srand(seed);
    cnt[0] = cnt[1] = 2 * n;
    start(board, n);
    for (int i = 0; i < steps; i++) {
        int ix, iy;
        const char turn = (i % 2 == 0) ? '1' : '2';
        do {
            ix = rnd(0, n);
            iy = rnd(0, n);
        } while (board[ix][iy] != turn);
        if (!capture(board, ix, iy, n)) {
            move(board, ix, iy, n);
        }
        }
    print(board, n);
    printf("%d %d\n", cnt[0], cnt[1]);

    return 0;
}