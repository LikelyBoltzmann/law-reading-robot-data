#
# old code to be removed
#


# from typing import Any

# def get_data_from_rss_feeds() -> Any: # TODO: Determine the return type
#     """
#     Gets the data from the RSS feeds
#     :return: Raw data from the RSS feeds, in a format that can be processed
#     """
#     raise NotImplementedError

# def process_raw_rss_feed_data(raw_data: Any) -> Any: # TODO: Determine the return type and type of raw_data
#     """
#     Processes the raw data from the RSS feeds, extracting relevant information from the raw data.
#     :param raw_data:
#     :return: Unknown. Possibly list of dictionaries with keys being the sub-item names and values being the values for
#     each sub-item (e.g., like description)
#     """
#     raise NotImplementedError

# def write_processed_rss_feed_data_to_csv(processed_data: Any) -> None:  # TODO: Determine the type of processed_data
#     """
#     Writes the processed data to a CSV file, with the name of the CSV file being the name of the RSS feed as well as the
#     date the data was retrieved.
#     :param processed_data: 
#     :return: None
#     """
#     raise NotImplementedError

# if __name__ == "__main__":
#     raw_data = get_data_from_rss_feeds()
#     processed_data = process_raw_rss_feed_data(raw_data)
#     write_processed_rss_feed_data_to_csv(processed_data)