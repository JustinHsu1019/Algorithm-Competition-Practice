// https://zerojudge.tw/ShowProblem?problemid=b964

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 1000

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int studentList[MAX_STUDENTS];
    int studentNum;
    char line[4096];
    char *token;
    const char *delimiter = " ";
    
    while (scanf("%d\n", &studentNum) != EOF) {
        int great[MAX_STUDENTS] = {0};
        int nope[MAX_STUDENTS] = {0};
        int greatNum = 0;
        int nopeNum = 0;

        if(fgets(line, sizeof(line), stdin) == NULL) {
            break;
        }

        token = strtok(line, delimiter);
        int i = 0;
        while (token != NULL) {
            studentList[i] = atoi(token);
            token = strtok(NULL, delimiter);
            i++;
        }

        qsort(studentList, studentNum, sizeof(int), compare);

        for (i = 0; i < studentNum; i++) {
            if (studentList[i] < 60) {
                nope[nopeNum++] = studentList[i];
            } else {
                great[greatNum++] = studentList[i];
            }
        }

        for (i = 0; i < studentNum; i++) {
            printf("%d ", studentList[i]);
        }
        printf("\n");

        if (nopeNum == 0) {
            printf("best case\n");
        } else {
            printf("%d\n", nope[nopeNum - 1]);
        }

        if (greatNum == 0) {
            printf("worst case\n");
        } else {
            printf("%d\n", great[0]);
        }
    }

    return 0;
}
