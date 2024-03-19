import pandas as pd 
import numpy as np

veri=pd.DataFrame(pd.read_excel("{YourData}"))
veri2=veri.pivot_table(values="Yas",columns=["Cinsiyet","Kan"],aggfunc=np.mean,index="İl")

print(veri2)


# veri2=veri.pivot_table(values="Yas",columns="Cinsiyet",aggfunc=len)
# # Cinsiyet  Erkek  Kadın
# # Yas        2361   2639

# veri2=veri.pivot_table(values="Yas",columns="Cinsiyet",aggfunc=sum)
# # Cinsiyet   Erkek   Kadın
# # Yas       106913  120273

# veri2=veri.pivot_table(values="Yas",columns="Cinsiyet",aggfunc=np.mean)
# # Cinsiyet      Erkek      Kadın
# # Yas       45.282931  45.575218

# veri2=veri.pivot_table(values="Yas",columns=["Cinsiyet","Kan"],aggfunc=np.mean)
# # Cinsiyet      Erkek                                                        ...      Kadın                                                      
# # Kan          0 Rh +     0 Rh -    A Rh +     A Rh -    AB Rh +    AB Rh -  ...     A Rh +     A Rh -    AB Rh +   AB Rh -     B Rh +     B Rh -
# # Yas       45.695971  45.371336  44.83908  44.823529  44.527586  46.693603  ...  45.674121  46.728435  45.387574  46.10951  45.084302  44.902655


# veri2=veri.pivot_table(values="Yas",columns=["Cinsiyet","Kan"],aggfunc=np.mean,index="İl")
# # Cinsiyet            Erkek                                              ...      Kadın                                            
# # Kan                0 Rh +     0 Rh -     A Rh +     A Rh -    AB Rh +  ...     A Rh -    AB Rh +    AB Rh -     B Rh +     B Rh -
# # İl                                                                     ...                                                       
# # Adana           55.500000  30.500000  48.000000  42.000000  35.000000  ...  36.250000  29.166667  48.666667  30.000000  39.400000
# # Adıyaman        47.400000  53.666667  41.000000  40.800000  44.666667  ...  53.500000  47.500000        NaN  42.333333  31.000000
# # Afyonkarahisar  50.666667  46.333333  63.000000  52.000000  34.833333  ...  53.333333  19.500000  49.250000  37.333333  40.250000
# # Aksaray         40.400000  49.000000  40.750000  56.000000  46.000000  ...        NaN  56.750000  53.000000  46.250000  36.666667
# # Amasya          46.000000  53.750000  41.666667  53.000000  31.000000  ...  37.800000  45.400000  46.750000  35.333333  40.800000
# # ...                   ...        ...        ...        ...        ...  ...        ...        ...        ...        ...        ...
# # Çorum           34.000000        NaN  41.000000  47.750000  50.500000  ...  41.428571  41.000000  45.000000  60.250000  32.500000
# # İstanbul        53.666667  55.500000  33.500000  41.666667  44.166667  ...  46.000000  45.800000  38.000000  45.400000  40.000000
# # İzmir           50.750000  50.250000  33.000000  31.750000  28.500000  ...  39.800000  50.000000  57.000000  43.857143  52.166667
# # Şanlıurfa       60.500000  29.500000  28.750000  49.400000  53.375000  ...  52.333333  51.500000  43.100000  56.000000  41.500000
# # Şırnak          50.000000  34.500000  71.000000  45.333333  73.000000  ...  46.500000  35.666667  44.250000  36.750000  50.800000


