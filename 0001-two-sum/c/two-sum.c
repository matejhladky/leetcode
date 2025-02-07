#include <stdio.h>

int* twoSum(int* nums, int numSize, int target, int* returnSize) {
  for (int i = 0; i < numSize; i++) {
    for (int j = i + 1; j < numSize; j++) {
      if (*(nums + i) + *(nums + j) == target) { // pointer arithmetic instead of indexing
        int* result = (int*)malloc(2 * sizeof(int));
        result[0] = i;
        result[1] = j;
        *returnSize = 2;
        return result;
      }
    }
  }
  *returnSize = 0;
  return malloc(sizeof(int) * 0);
}

int* twoSum(int* nums, int numSize, int target, int* returnSize) {
  struct hashTable {
    int key;
    int value;
    UT_hash_handle hh; // macro from the uthash library
  } *hashTable = NULL, *item, *tmpItem; // pointer to the ht itself

  for (int i = 0; i < numSize; i++) {
    HASH_FIND_INT(hashTable, &nums[i], item);
    if (item) {
      int *result = malloc(sizeof(int) * 2);
      result[0] = item->value;
      result[1] = i;
      *returnSize = 2;
      HASH_ITER(hh, hashTable, item, tmpItem) { // cleanup
        HASH_DEL(hashTable, item);
        free(item);
      }
      return result;
    }
    item = malloc(sizeof(struct hashTable));
    item->key = target - nums[i];
    item->value = i;
    HASH_ADD_INT(hashTable, key, item);
  }
  HASH_ITER(hh, hashTable, item, tmpItem) { // cleanup
    HASH_DEL(hashTable, item);
    free(item);
  }
  *returnSize = 0;
  return malloc(sizeof(int) * 0);
}
