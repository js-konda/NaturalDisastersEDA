#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def opie(data):
    '''
    :parameter data dataframe
    :graph disasters appearance and their percentage relative to other disaters
    :use dictionary to count each disaster appeearance 
    :and plot it keys and values
    '''
    assert isinstance(data, pd.DataFrame)

    x={}
    for i in data['Disaster Type']:
        try:
            x[i]+=1
        except:
            x[i]=1
    
    explode = (0.1, 0,0,0,0,0,0) 
    tot= sum(x.values())
    n={}
    for i in x:
        if x[i]/tot > .046:
            n[i]=x[i]
        else:
            try:
                n['other']+=x[i]
            except:
                n['other']=x[i]
    n = dict(sorted(n.items(), key=lambda item: item[1], reverse=True))
    print(n)
    presentation_colors = plt.cm.Spectral(np.linspace(0, 1, 9))[::-1]
    presentation_colors = np.vstack((presentation_colors,cls.to_rgba("grey")))
    colorsfixed = []
    colorsfixed.append(presentation_colors[4])
    colorsfixed.append(presentation_colors[6])
    colorsfixed.append(presentation_colors[2])
    colorsfixed.append(presentation_colors[9])
    colorsfixed.append(presentation_colors[1])
    colorsfixed.append(presentation_colors[5])
    colorsfixed.append(presentation_colors[0])
    fig1, ax1 = plt.subplots()
    ax1.pie(n.values(), labels= n.keys(), autopct='%1.f%%', explode = explode,
        shadow=True, startangle=0, colors = colorsfixed, textprops={'fontsize': 14})
    fig1.set_size_inches(5, 5)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Total disasters',fontdict = {'fontsize' : 16})
    plt.show()


# In[ ]:


def stringpie(data,string):
    '''
    :parameter data dataframe and string str
    :graph the # caused by disasters and their percentage relative to other disaters
    :use a dictionary to calculate all the number relate to the string for each disaster
    :use a new dictionary to lower amount of keys to 4 to 6 
    :add all the lower tier disaster together and categorize them as other (by percentage)
    :plot the dict keys and values
    '''
    
    assert isinstance(data, pd.DataFrame)
    assert isinstance(string, str)
    assert len(string) > 3
    data[string]=data[string].fillna(0)
    a=zip(data['Disaster Type'])
    b=zip(data[string])
    dtlist=list(a)
    tdlist=list(b)
    l={}
    
    for i in range(len(dtlist)):
        
        if dtlist[i] in l:
            l[dtlist[i]]+=tdlist[i]
            
        else:
            l[dtlist[i]]=tdlist[i]
    
    
    x={}
    tresh= .04
    if string=='Total Deaths':
        tresh=.06
    for i in l:
        x[i]=sum(l[i])
    tot= sum(x.values())
    n={}
    for i in x:
        if x[i]/tot > tresh:
            n[i]=x[i]
        else:
            try:
                n['other']+=x[i]
            except:
                n['other']=x[i]
    n = dict(sorted(n.items(), key=lambda item: item[1], reverse=True))
    explode =[0.1] + [0] * (len(n)-1)
    fig1, ax1 = plt.subplots()
    presentation_colors = plt.cm.Spectral(np.linspace(0, 1, 9))[::-1]
    presentation_colors = np.vstack((presentation_colors,cls.to_rgba("grey")))
    
    colorsfixed = []
    if (string == 'Total Damages (\'000 US$)'):
        colorsfixed.append(presentation_colors[6])
        colorsfixed.append(presentation_colors[4])
        colorsfixed.append(presentation_colors[1])
        colorsfixed.append(presentation_colors[9])
        colorsfixed.append(presentation_colors[0])
    else: 
        colorsfixed.append(presentation_colors[1])
        colorsfixed.append(presentation_colors[6])
        colorsfixed.append(presentation_colors[0])
        colorsfixed.append(presentation_colors[4])
        colorsfixed.append(presentation_colors[9])
        colorsfixed.append(presentation_colors[2])
    labels = [str(each).strip("(").strip(")").strip(",").strip("'") for each in n.keys()]
    ax1.pie(n.values(), labels= labels, explode=explode, autopct='%1.f%%',
        shadow=True, startangle=0, colors = colorsfixed, textprops={'fontsize': 14})
    ax1.axis('equal')
    fig1.set_size_inches(5, 5)
    plt.title('Which disaster causes the ' + string, fontdict = {'fontsize' : 16})
    plt.show()


# In[ ]:





# In[ ]:




