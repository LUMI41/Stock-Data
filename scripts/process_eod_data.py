import numpy as np
import os
from tqdm import tqdm
import pandas as pd

def load_EOD_data(data_path, market_name, tickers, steps=1):
    eod_data = []
    masks = []
    ground_truth = []
    base_price = []
    for index, ticker in enumerate(tqdm(tickers)):
        single_EOD = np.genfromtxt(
            os.path.join(data_path, market_name + '_' + ticker + '_1.csv'),
            dtype=np.float32, delimiter=',', skip_header=False
        )
        if market_name == 'NASDAQ':
            # remove the last day since lots of missing data
            single_EOD = single_EOD[:-1, :]
        if index == 0:
            print('single EOD data shape:', single_EOD.shape)
            eod_data = np.zeros([len(tickers), single_EOD.shape[0],
                                 single_EOD.shape[1] - 1], dtype=np.float32)
            masks = np.ones([len(tickers), single_EOD.shape[0]],
                            dtype=np.float32)
            ground_truth = np.zeros([len(tickers), single_EOD.shape[0]],
                                    dtype=np.float32)
            base_price = np.zeros([len(tickers), single_EOD.shape[0]],
                                  dtype=np.float32)
        for row in range(single_EOD.shape[0]):
            if abs(single_EOD[row][-1] + 1234) < 1e-8:
                masks[index][row] = 0.0
            elif row > steps - 1 and abs(single_EOD[row - steps][-1] + 1234) \
                    > 1e-8:
                ground_truth[index][row] = \
                    (single_EOD[row][-1] - single_EOD[row - steps][-1]) / \
                    single_EOD[row - steps][-1]
            for col in range(single_EOD.shape[1]):
                if abs(single_EOD[row][col] + 1234) < 1e-8:
                    single_EOD[row][col] = 1.1
        eod_data[index, :, :] = single_EOD[:, 1:]
        base_price[index, :] = single_EOD[:, -1]
    return eod_data, masks, ground_truth, base_price


if __name__ == '__main__':
    steps = 1
    market_name = 'TSE'
    data_path = '../../../data/processed_TSE_wo_normalizing/'
    tickers_fname = f"../wiki/tickers_tse_qualified_prime.csv"
    tickers = pd.read_csv(tickers_fname)
    tickers = tickers['Local Code'].astype(str)
    batch_size = len(tickers)
    print('#tickers selected:', len(tickers))
    eod_data, mask_data, gt_data, price_data = load_EOD_data(data_path, market_name, tickers, steps)
    # np.save('../../../../sthan-sr-aaai-main/tse/eod_data_tse.npy', eod_data)
    # np.save('../../../../sthan-sr-aaai-main/tse/mask_data_tse.npy', mask_data)
    # np.save('../../../../sthan-sr-aaai-main/tse/gt_data_tse.npy', gt_data)
    # np.save('../../../../sthan-sr-aaai-main/tse/price_data_tse.npy', price_data)
    np.save('../../../data/TSE_wo_normalizing/eod_data.npy', eod_data)
    np.save('../../../data/TSE_wo_normalizing/mask_data.npy', mask_data)
    np.save('../../../data/TSE_wo_normalizing/gt_data.npy', gt_data)
    np.save('../../../data/TSE_wo_normalizing/price_data.npy', price_data)
