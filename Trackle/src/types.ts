export interface Network{
    connections: any[];
    speed: any[];
    addrs: any;
    net_io_counters: any;
    hostname: string;
    boot_time: string;
}

export interface Hardware{
    cpu_freq: any;
    cpu_stats: any;
    cpu_count: any;
    cpu_percentage: any;
    virtual_memory: any;
    swap_memory: any;
    loadavg: any;
    disk_partitions: any;
    disk_usage: any;
    disk_io_counters: any;
}
