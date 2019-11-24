import multiprocessing

manager = multiprocessing.Manager()
return_dict = manager.dict()


def processor(classifier, images):
    model = classifier()
    return_dict['1'] = model.classify(images)


def tfpred(classifier, images):

    p = multiprocessing.Process(target=tfpred, args=(classifier,[images]))
    p.start()
    p.join()
    ret_values = return_dict.values()
    return_dict = manager.dict()
    return ret_values
