#include <stdio.h>
#include <stdlib.h>

int main() {
    int N;
    scanf("%d", &N);
    
    int* priorities = (int*)malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) {
        scanf("%d", &priorities[i]);
    }
    
    int K;
    scanf("%d", &K);
    K--; // Convert to 0-based index

    int served_count = 0;
    int served[N]; // To track served orders
    for (int i = 0; i < N; i++) {
        served[i] = 0; // Initialize all as not served
    }

    while (1) {
        // Find the index of the highest priority order that has not been served
        int max_index = -1;
        for (int i = 0; i < N; i++) {
            if (!served[i] && (max_index == -1 || priorities[i] > priorities[max_index])) {
                max_index = i;
            }
        }

        // Serve the order at max_index
        served_count++;
        served[max_index] = 1; // Mark as served

        // Check if the served order is Raj's friend's order
        if (max_index == K) {
            printf("%d\n", served_count);
            break;
        }

        // Increment the priority of all remaining orders before max_index
        for (int i = 0; i < max_index; i++) {
            if (!served[i]) {
                priorities[i]++;
            }
        }
    }

    free(priorities);
    return 0;
}
