#!/usr/bin/env python
# coding: utf-8

# In[1]:


class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def _calculate_total_and_count(self):
        total = sum(self.data)
        count = len(self.data)
        return total, count

    def _calculate_total(self):
        total, _ = self._calculate_total_and_count()
        return total

    def _calculate_average(self):
        total, count = self._calculate_total_and_count()
        return total / count if count != 0 else 0

    def calculate_total(self):
        return self._calculate_total()

    def calculate_average(self):
        return self._calculate_average()

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None


# In[ ]:




