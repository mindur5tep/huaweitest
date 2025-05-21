#include <stdio.h>
#include <stdlib.h>

int main() {
    int N, W;

    // Read N and W
    scanf("%d %d", &N, &W);

    // Allocate memory for the trust sequence array
    int *trust_sequence = (int *)malloc(N * sizeof(int));

    // Read the trust sequence
    for (int i = 0; i < N; i++) {
        scanf("%d", &trust_sequence[i]);
    }

    // Calculate the minimum trust score for each window of size W
    for (int i = 0; i <= N - W; i++) {
        int min_value = trust_sequence[i];

        // Find the minimum in the current window of size W
        for (int j = i; j < i + W; j++) {
            if (trust_sequence[j] < min_value) {
                min_value = trust_sequence[j];
            }
        }

        // Print the minimum value for this window
        printf("%d", min_value);

        // Add space between outputs, but not after the last value
        if (i < N - W) {
            printf(" ");
        }
    }

    // Free the allocated memory
    free(trust_sequence);

    return 0;
}
