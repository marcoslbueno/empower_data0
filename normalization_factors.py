
# # # # # # # # # # # # # # # # # #
#                                 #
#         ATTENTION GAME          #
#                                 #
# # # # # # # # # # # # # # # # # #

ATTENTION_FACTORS = {
    # "columns" : ['sus_attention', 'cog_processing_speed_ms', 'errorpresent',
    #             'errorabsent', 'impulse_control', 'late_response', 'RT_late_ms',
    #             'RT_incorrect_ms', 'meanRT_ms', 'accuracy', 'reg_attention'],
"columns" : ['sus_attention', 'cog_processing_speed_ms', 'errorpresent',
                'errorabsent', 'late_response', 'RT_late_ms',
                'RT_incorrect_ms', 'meanRT_ms', 'accuracy', 'reg_attention'],
    "sus_attention": {
        "min": [0, 0, 0],
        "max": [1, 1, 1]
    },
    "cog_processing_speed_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "RT_late_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "RT_incorrect_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "meanRT_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "accuracy":{
        "min": [0, 0, 0],
        "max": [60, 60, 60]
    },
    "errorpresent": {
        "min": [0, 0, 0],
        "max": [18, 18, 18]
    },
    "late_response":{
        "min": [0, 0, 0],
        "max": [60, 60, 60]
    },
    # "impulse_control":{
    #     "min": [0, 0, 0],
    #     "max": [42, 42, 42]
    # },
    "errorabsent":{
        "min": [0, 0, 0],
        "max": [42, 42, 42]
    }
}

ATTENTION_NEUROTYPICAL_FACTORS = {
    # "columns" : ['sus_attention', 'cog_processing_speed_ms', 'errorpresent',
    #             'errorabsent', 'impulse_control', 'late_response', 'RT_late_ms',
    #             'RT_incorrect_ms', 'meanRT_ms', 'accuracy', 'reg_attention'],
"columns" : ['sus_attention', 'cog_processing_speed_ms', 'errorpresent',
                'errorabsent', 'late_response', 'RT_late_ms',
                'RT_incorrect_ms', 'meanRT_ms', 'accuracy', 'reg_attention'],
    "sus_attention": {
        "min": [0, 0, 0],
        "max": [18, 18, 18]
    },
    "cog_processing_speed_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "RT_late_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "RT_incorrect_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "meanRT_ms": {
        "min": [0, 0, 0],
        "max": [2500, 2000, 1500]
    },
    "accuracy":{
        "min": [0, 0, 0],
        "max": [18, 18, 18]
    },
    "errorpresent": {
        "min": [0, 0, 0],
        "max": [18, 18, 18]
    },
    "late_response":{
        "min": [0, 0, 0],
        "max": [18, 18, 18]
    },
    # "impulse_control":{
    #     "min": [0, 0, 0],
    #     "max": [42, 42, 42]
    # },
    "errorabsent":{
        "min": [0, 0, 0],
        "max": [42, 42, 42]
    }
}

# # # # # # # # # # # # # # # # # #
#                                 #
#         WORKMEMORY GAME         #
#                                 #
# # # # # # # # # # # # # # # # # #

WORKMEMORY_FACTORS = {
    "columns": ['order_recall', 'order_recall_per_trial', 'wrong_order_correct_recall', 'wrong_order_correct_recall_per_trial',
                'wm_retention', 'meanRT_sort', 'meanRT_memory','RT_correct', 'RT_incorrect'],
    "order_recall": {
        "min": [0, 0, 0],
        "max": [10, 15, 20]
    },
    "order_recall_per_trial": {
        "min": [0, 0, 0],
        "max": [2, 3, 4]
    },
    "wrong_order_correct_recall": {
        "min": [0, 0, 0],
        "max": [10, 15, 20]
    },
    "wrong_order_correct_recall_per_trial": {
        "min": [0, 0, 0],
        "max": [2, 3, 4]
    },
    "wm_retention": {
        "min": [0, 0, 0],
        "max": [2, 3, 4]
    },
    "meanRT_sort":{
        "min": [0, 0, 0],
        # "log-max": [6, 6, 6]
        "max": [12000, 12000, 12000]
    },
    "meanRT_memory": {
        "min": [0, 0, 0],
        "log-max": [6, 6, 6]
        # "max": [12000, 12000, 12000]
    },
    "RT_correct":{
        "min": [0, 0, 0],
        # "log-max": [6, 6, 6]
        "max": [12000, 12000, 12000]
    },
    "RT_incorrect":{
        "min": [0, 0, 0],
        # "log-max": [6, 6, 6]
        "max": [12000, 12000, 12000]
    }
}

# # # # # # # # # # # # # # # # # #
#                                 #
#           COGFLEX GAME          #
#                                 #
# # # # # # # # # # # # # # # # # #

COGNITIVEFLEXIBILITY_FACTORS = {
    "columns": ['studentID', 'activityID', 'activitytype', 'level', 'cog_adaptability',
       'correct_categories', 'trials_total', 'set_shifting',
       'perseverative_responses', 'errors', 'errors_per_trial', 'hits',
       'hits_per_trial', 'rule_maintain', 'meanRT', 'RT_correct',
       'RT_incorrect'],

  "cog_adaptability":{  #changed to 9 because of data
        "min": [9,9,9],
        "max": [90,90,90]
  },
  "correct_categories": {
    "min": [0,0,0],
    "max": [6,6,6]
  },
  "trials_total": {
    "min": [60,60,60],
    "max": [90,90,90]
  },
  "set_shifting": {
    "min": [0,0,0],
    "max": [6,6,6]
  },
  "perseverative_responses": {
    "min": [0,0,0],
    "max": [6,6,6]
  },
  "errors": {
    "min": [0,0,0],
    "max": [90,90,90]
  },
  "errors_per_trial": {
    "min": [0,0,0],
    "max": [90,90,90]
  },
      # ,"errors_per_trial": {
  #   "min": [0,0,0],
  #   "max": [90,90,90]
  # },
  "hits": {
    "min": [0,0,0],
    "max": [87,87,87]
  },
  "hits_per_trial": {
    "min": [0,0,0],
    "max": [81,81,81]
  },
  "rule_maintain": {
    "min": [0,0,0],
    "max": [90,90,90]
  },
  "meanRT": {
    "min": [0, 0, 0],
    # "log-max": [6, 6, 6]
    "max": [10000, 10000, 10000]
  },
  "RT_correct": {
    "min": [0, 0, 0],
    # "log-max": [6, 6, 6]
    "max": [10000, 10000, 10000]
  },
  "RT_incorrect": {
    "min": [0, 0, 0],
    # "log-max": [6, 6, 6]
    "max": [10000, 10000, 10000]
  }
}

# # # # # # # # # # # # # # # # # #
#                                 #
#        INHIBITION GAME          #
#                                 #
# # # # # # # # # # # # # # # # # #

INHIBITION_FACTORS = {
    "columns" : ['omission_errors', 'inhib_score', 'resilience', 'all_errors', 'meanRT',
       'RT_correct', 'RT_incorrect', 'task_process_congruent',
       'task_process_incongruent', 'RT_congruent', 'RT_incongruent'],

  "omission_errors": {
    "min": [0,0,0],
    "max": [12,12,12]
  },
  "inhib_score": {
     "min": [0,0,0],
    "max": [12,12,12]
  },
  "all_errors": {
     "min": [0,0,0],
    "max": [12,12,12]
  },
  "resilience": {
      "min": [0, 0, 0],
      "max": [12, 12, 12]
  },
  "meanRT": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "RT_correct": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "RT_incorrect": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "task_process_congruent": {
    "min": [0,0,0],
    "max": [12, 12, 12]
  },
  "task_process_incongruent": {
    "min": [0,0,0],
    "max": [12, 12, 12]
  },
  "RT_congruent": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "RT_incongruent": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  }
}

INHIBITION_Neurotypical_FACTORS = {
    "columns" : ['omission_errors', 'inhib_score', 'resilience', 'all_errors', 'meanRT',
       'RT_correct', 'RT_incorrect', 'task_process_congruent',
       'task_process_incongruent', 'RT_congruent', 'RT_incongruent'],

  "omission_errors": {
    "min": [0,0,0],
    "max": [12,12,12]
  },
  "inhib_score": {
     "min": [0,0,0],
    "max": [12,12,12]
  },
  "resilience": {
      "min": [0, 0, 0],
      "max": [12, 12, 12]
  },
  "meanRT": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "RT_correct": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "RT_incorrect": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "task_process_congruent": {
    "min": [0,0,0],
    "max": [12, 12, 12]
  },
  "task_process_incongruent": {
    "min": [0,0,0],
    "max": [12, 12, 12]
  },
  "RT_congruent": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  },
  "RT_incongruent": {
    "min": [0,0,0],
    "max": [20000, 2500, 2000]
  }
}


# # # # # # # # # # # # # # # # # #
#                                 #
#    DELAY GRATIFICATION GAME     #
#                                 #
# # # # # # # # # # # # # # # # # #
DELAYGRAT_FACTORS = {
    "columns" : ['total_waited'],

  "total_waited": {
    "min": [0,0,0],
    "max": [1,1,1]
  }
}

# # # # # # # # # # # # # # # # # #
#                                 #
#       EMOTION WHEEL GAME        #
#                                 #
# # # # # # # # # # # # # # # # # #
EMOTWHEEL_FACTORS = {
    "columns" : ['correctemotion','emotion','emotionIntensity','neutralclick','naming','understanding','regulation'],

  "correctemotion": {
    "min": [0,0],
    "max": [1,1]
  },
  "emotion": {
    "min": [-1,-1],
    "max": [8,8]
  },
  "emotionIntensity": {
    "min": [0,0],
    "max": [5,5]
  },
  "neutralclick": {
    "min": [0,0],
    "max": [100,100] # this is based on the number of neutral clicks in the sample
  },
  "naming": {
    "min": [0,0],
    "max": [100,100] # this is based on the number of neutral clicks in the sample
  },
  "understanding": {
    "min": [0,0],
    "max": [100,100] # this is based on the number of neutral clicks in the sample
  },
 "regulation": {
    "min": [0,0],
    "max": [1,1] # this is based on the number of neutral clicks in the sample
  },
}

# # # # # # # # # # # # # # # # # #
#                                 #
#       EMOTION CORNHOLE GAME     #
#                                 #
# # # # # # # # # # # # # # # # # #
EMOTCORNHOLE_FACTORS = {
    "columns" : ['correctemotion','emotion','emotionIntensity','neutralclick','naming','understanding','regulation'],

  "correctemotion": {
    "min": [0,0],
    "max": [1,1]
  },
  "emotion": {
    "min": [-1,-1],
    "max": [8,8]
  },
  "emotionIntensity": {
    "min": [0,0],
    "max": [5,5]
  },
  "neutralclick": {
    "min": [0,0],
    "max": [100,100] # this is based on the number of neutral clicks in the sample
  },
  "naming": {
    "min": [0,0],
    "max": [100,100] # this is based on the number of neutral clicks in the sample
  },
  "understanding": {
    "min": [0,0],
    "max": [100,100] # this is based on the number of neutral clicks in the sample
  },
 "regulation": {
    "min": [0,0],
    "max": [1,1] # this is based on the number of neutral clicks in the sample
  },
}

# # # # # # # # # # # # # # # # # #
#                                 #
#         EMOTION EGG GAME        #
#                                 #
# # # # # # # # # # # # # # # # # #
EMOTCORNHOLE_FACTORS = {
    "columns": [
        'emotion','emotionIntensity','understanding','regulation'],
        # 'meanRT_Eggs', 'emotion','emotionIntensity','understanding','regulation'],
    # "meanRT_Eggs":{
    #     "min": [0, 0],
    #     "max": [1000, 1000]
    # },
    "emotion": {
        "min": [-1, -1],
        "max": [8, 8]
    },
    "emotionIntensity": {
        "min": [0, 0],
        "max": [5, 5]
    },
  "understanding": {
    "min": [0,0],
    "max": [100,100]
  },
 "regulation": {
    "min": [0,0],
    "max": [1,1]
  },
}