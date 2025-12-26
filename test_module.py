#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import matplotlib as mpl
import sea_level_predictor


class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_draw_plot_returns_figure(self):
        fig = sea_level_predictor.draw_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)


if __name__ == "__main__":
    unittest.main()


# In[ ]:




