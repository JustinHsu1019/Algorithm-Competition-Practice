// https://zerojudge.tw/ShowProblem?problemid=b964

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class N1_Score_100 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> studentList, great, nope;

        while (scanner.hasNextInt()) {
            int studentNum = scanner.nextInt();
            scanner.nextLine();
            studentList = new ArrayList<>();
            great = new ArrayList<>();
            nope = new ArrayList<>();
            String studentInp = scanner.nextLine();
            String[] studentStrList = studentInp.split(" ");

            for (String s : studentStrList) {
                int score = Integer.parseInt(s);
                studentList.add(score);
            }

            Collections.sort(studentList);
            StringBuilder resultStr = new StringBuilder();

            for (int score : studentList) {
                resultStr.append(score).append(" ");
                if (0 <= score && score < 60) {
                    nope.add(score);
                } else if (60 <= score && score <= 100) {
                    great.add(score);
                }
            }

            System.out.println(resultStr.toString().trim());

            Collections.sort(nope);
            Collections.sort(great);

            if (nope.isEmpty()) {
                System.out.println("best case");
            } else {
                System.out.println(nope.get(nope.size() - 1));
            }

            if (great.isEmpty()) {
                System.out.println("worst case");
            } else {
                System.out.println(great.get(0));
            }
        }
        scanner.close();
    }
}
