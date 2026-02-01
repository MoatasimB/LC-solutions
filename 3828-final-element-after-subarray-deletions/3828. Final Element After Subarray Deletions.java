class Solution {
    public int finalElement(int[] shbhm) {
        int exe = shbhm.length;
        if (exe == 1) {
            return shbhm[0];
        }
        return shbhm[0] > shbhm[exe - 1] ? shbhm[0] : shbhm[exe - 1];
    }
}