import java.util.Scanner;

public class KnapSack {

	static int n;
	static int[] w;
	static int[] p;
	int tmp;
	static int C;
	static int[][] dp;
	static Scanner s = new Scanner(System.in);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the Capacity C: ");
		C = s.nextInt();
		System.out.println("Enter number of items");
		n = s.nextInt();

		w = new int[n + 1];
		dp = new int[n + 1][C + 1];
		p = new int[n + 1];
		System.out.println("----Enter the item weights----");
		for (int i = 1; i < n + 1; i++) {
			System.out.printf("w[%d]: ", i - 1);
			w[i] = s.nextInt();
			System.out.printf("p[%d]: ", i - 1);
			p[i] = s.nextInt();
			System.out.println();
		}

		System.out.println("performing knapsack algo...");
		KS();
		System.out.printf("the max profit is: %d \n", dp[n][C]);

		// find the solution set.

		for (int i = 0; i < n + 1; i++) {
			for (int j = 0; j < C + 1; j++) {
				System.out.printf("%d ", dp[i][j]);
			}
			System.out.println();
		}
		while (n > 1) {
			if (dp[n][C] > dp[n - 1][C]) {
				System.out.printf("item %d \n", n - 1);
			}
			n--;
		}

	}

	public static void KS() {
//
//		for (int i = 0; i < n + 1; i++) {
//			dp[i][0] = 0;
//		}
//
//		for (int i = 1; i < C + 1; i++) {
//			dp[0][i] = 0;
//		}

		for (int i = 1; i < n + 1; i++) {
			for (int j = 1; j < C + 1; j++) {
				dp[i][j] = dp[i - 1][j];
				if (w[i] <= j) {
					if (dp[i][j] < dp[i - 1][j - w[i]] + p[i]) {
						dp[i][j] = dp[i - 1][j - w[i]] + p[i];
					}
				}
			}
		}

	}

}
