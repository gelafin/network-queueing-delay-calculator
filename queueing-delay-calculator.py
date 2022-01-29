# Author: Mark Mendez
# Date: 01/29/2022


def calculate_queuing_delay(packet_size_in_bytes: int, rate_in_Gbps: float, packet_number: int):
    """
    Calculates network queueing delay
    :param packet_size_in_bytes: bytes per packet
    :param rate_in_Gbps: total connection speed / link transmission rate, in Gbps
    :param packet_number: packet to find queueing delay for (number of previous packets + 1)
    :return: queuing delay in milliseconds
    """
    # convert units
    packet_size_in_bits = packet_size_in_bytes * 8
    rate_in_bps = rate_in_Gbps * 1000 * 1000 * 1000  # convert from Gbps to Mbps to Kbps to bps

    # calculate rate per packet
    transmission_time_per_packet_in_ms = packet_size_in_bits / rate_in_bps * 1000  # * 1000 to convert to ms

    # calculate queuing delay
    previous_packet_count = packet_number - 1
    queueing_delay = transmission_time_per_packet_in_ms * previous_packet_count

    return queueing_delay


if __name__ == '__main__':
    # test
    packet_size_in_MiB = 5  # set to None if entering file_size_in_bytes
    packet_size_in_bytes = None  # set to None if entering file_size_in_MiB
    rate_in_Gbps = 2.1
    packet_number = 48  # packet to find queueing delay for

    packet_size_in_bytes = packet_size_in_MiB * 1024 * 1024 if packet_size_in_MiB is not None else packet_size_in_bytes
    result = calculate_queuing_delay(packet_size_in_bytes, rate_in_Gbps, packet_number)
    print('\nqueueing delay: ', result)

