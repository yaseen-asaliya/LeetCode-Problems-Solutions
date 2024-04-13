class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int sizeN1 = nums1.length, sizeN2 = nums2.length, index1 = 0, index2 = 0, k = 0;
    int[] res = new int[sizeN1 + sizeN2];

    while (index1 < sizeN1 || index2 < sizeN2) {
        if (index1 != sizeN1 && index2 != sizeN2) {
            if (nums1[index1] > nums2[index2]) {
                res[k++] = nums2[index2++];
            } else {
                res[k++] = nums1[index1++];
            }
        } else if (index1 == sizeN1) {
            while (index2 != sizeN2) {
                res[k++] = nums2[index2++];
            }
            break;
        } else if (index2 == sizeN2) {
            while (index1 != sizeN1) {
                res[k++] = nums1[index1++];
            }
            break;
        }
    }

    int newLen = sizeN1 + sizeN2;
    if (newLen % 2 == 0) {
        return (res[newLen / 2 - 1] + res[newLen / 2]) / 2.0;
    } else {
        return res[newLen / 2];
    }
}

}