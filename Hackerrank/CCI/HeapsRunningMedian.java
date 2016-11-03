

 import java.io.*;
 import java.util.*;
 import java.text.*;
 import java.math.*;
 import java.util.regex.*;

public class Solution {
    private Comparator<Integer> maxHeapComparator;
    private Comparator<Integer> minHeapComparator;

    private PriorityQueue<Integer> maxQueue, minQueue;

    public Solution() {
        maxHeapComparator = Comparator.reverseOrder();
        minHeapComparator = Comparator.naturalOrder();

        maxQueue = new PriorityQueue<Integer>(maxHeapComparator);
        minQueue = new PriorityQueue<Integer>(minHeapComparator);
    }

    public void addNewNumber(int randomNumber) {
        if (maxQueue.size() == minQueue.size()) {
            if (minQueue.peek() != null && randomNumber > minQueue.peek()) {
                maxQueue.offer(minQueue.poll());
                minQueue.offer(randomNumber);
            } else {
                maxQueue.offer(randomNumber);
            }
        } else {
            if (randomNumber < maxQueue.peek()) {
                minQueue.offer(maxQueue.poll());
                maxQueue.offer(randomNumber);
            } else {
                minQueue.offer(randomNumber);
            }
        }
    }

    public double getMedian() {
        if (maxQueue.isEmpty()) {
            return 0;
        } else if (maxQueue.size() == minQueue.size()) {
            return ((double)minQueue.peek() + (double)maxQueue.peek()) / 2.0;
        }  else {
            return maxQueue.peek();
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Solution solution = new Solution();
        for(int a_i=0; a_i < n; a_i++){
            solution.addNewNumber(in.nextInt());
            System.out.println(solution.getMedian());
        }
    }
 }

