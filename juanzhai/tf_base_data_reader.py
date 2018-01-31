class TFBaseDataReader():

    def describe(self, logger):
        raise NotImplementedError('subclass must implement this')

    def gen_train(self, batch_size):
        raise NotImplementedError('subclass must implement this')

    def gen_val(self, batch_size):
        raise NotImplementedError('subclass must implement this')

    def gen_test(self, batch_size):
        raise NotImplementedError('subclass must implement this')
