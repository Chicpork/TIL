# elasticsearch

## elasticsearch 설정파일 예시

``` yml
cluster.name: fastcampus-cluster
node.name: es1
node.roles: ["master", "data"]
```

- cluster.name과 node.name에 의해 클러스터화가 자동으로 이뤄지기때문에 중요하다.
- `cluster.name`
  - 이 설정이 같은 node가 실행되면 동일 클러스터로 구성된다.
- `node.name`
  - 노드의 용도와 목적을 이해 하기 위한 사람이 읽을 수 있는 식별자로 작성하면 좋다.
- Cluster 환경 구동시 참고 설정
  - `discovery.type`
    - cluster.initial_master_nodes와 함께 사용 불가
    - 이 설정이 등록되어 있으면 singel-node라는 값으로 지정이 되고 단일 노드 구성이 이루어짐
  - `discovery.seed_hosts`
    - Clustering을 위한 노드 목록 작성
  - `cluster.initial_master_nodes`
    - master 역할을 가진 노드 목록 작성
    - master 구성은 최소 3개 이상의 쿼럼 구성을 추천
- Heap 설정
  - elasticsearch는 jvm위에서 동작하므로 실행 시 Heap 설정.
  - 이 경우, 시스템 메모리를 전용으로 안정적으로 사용하기 위해 아래와 같은 설정 사용추천
  - `bootstrap.memory_locak:true`
    - Elasticsearch 는 HTTP 통신과 Transport 통신 둘 다 지원
    - 노드간 통신은 transport로 이루어지며, 통신을 위한 port 설정과 content 전송에 따른 compression 설정 등이 가능함
  - `http.port`
    - 기본 9200 포트로 선언 되며, 지정시 해당값으로 할당
  - `http.max_content_length`
    - RESTful API 요청 시 실제 저장된 문서의 크기가 클 경우, 100MB (HTTP Request Body Size)를 넘어가는 경우 -> 크기를 적당히 조절
    - 주의) 네트워크의 bandwidth를 많이 사용하지 않기(네트워크 병목으로 성능 저하)
- HTTP 통신 설정
  - `http.max_initial_line_length`
    - HTTP URL 의 최대 크기 4KB
  - `http.max_header_size`
    - 허용하는 최대 Header 크기 (8KB)
  - `http.compression`
    - 압축전송 설정.
    - 기본 false 이나 true 로 설정 추천
    - B2C 형 서비스인 경우 API gateway를 별도로 두기 때문에 true로 설정해서 network 병목을 최소화 할 수 있음.
  - `http.compression_level`
    - 기본 3 설정, CPU 자원에 대한 소비가 많을수 있기 때문에 그대로 사용 권장(1 ~ 9)
  - `http.cors.enabled`
    - 기본 false로 설정
    - 이 설정을 통해서 Elasticsearch로의 요청에 대한 origin 점검 가능
    - true로 설정시 허용할 origin을 등록
  - `http.cors.allow-origin`
    - 요청에 대해 허용할 origin 등록(정규표현식 가능)
    - 요청 시 header에 origin 정보를 담아서 요청해야함.
- Transport 통신 설정
  - `transport.port`
    - 노드간 통신에 사용되는 포트.
    - 기본 9300
  - `transport.comporess`
    - 기본 false이며, local 통신이 기본이라 false로 설정해서 사용하는 것을 추천
- discovery 설정
  - 클러스터 구성 시, 각 노드를 발견하고 합류시키기 위한 설정
  - `gateway.expected_data_nodes`
    - 최소 실행 된 data node의 개수를 지정하기 위해 사용함
    - 클러스터가 재시작 될 때 in-service 전에 확인하기 위해 활용
    - 기본 값은 0이지만 in-service를 위해 최소 실행 된 data node의 수를 지정하여 사용
  - `gateway.recover_after_data_nodes`
    - recovery를 data node가 몇개나 올라온 이후 실행될지 결정하는 값
    - 클러스터가 재시작될 때 활용
    - 재시작 시 문제점 : 모든 master, data 노드가 클러스터에 join 되면서 동시에 recovery 작업을 수행 하게 되면 리소스를 많이 사용하게 되면서 hang이 걸릴 수도 있음.
    - 최소 규모의 데이터 노드가 실행 된 후에 recovery를 수행하도록 명시적으로 선언할것
- index 관련 설정
  - `action.auto_create_index`
    - 인덱스를 자동으로 설정해주는 옵션(기본 true)
    - 불필요한 index의 생성을 방지하고 싶다면 false로 설정
  - `action.destructive_requires_name`
    - 기본 false이기 때문에 누구나 생성된 index 삭제 가능
    - wildcard(*)로 삭제 요청시 전체 index가 삭제될수 있음.
    - 명시적으로 인덱스 이름으로 삭제 요청을 하도록 하고 싶다면, 이 설정을 확인하고 true로 설정
- xpack 관련 설정
  - `xpack.monitoring.collection.enabled`
    - 기본 false로 설정,
    - elasticsearch에 대한 모니터링을 하고자 한다면 true로 설정

---

## 노드의 역할

### 1. master(m)

- 클러스터의 상태를 변경
- 클러스터의 상태를 모든 노드에 게시
- 전역 클러스터 상태를 유지
- 샤드에 대한 할당과 클러스터 상태 변화 게시

### 2. data(d)

- 문서의 색인 및 저장
- 문서의 검색 및 분석(코디네이팅)

### 3. data_content(s)

- 색인과 검색 요청이 많은 경우

### 4. data_hot(h)

- 색인에 대한 요청이 많으며 자주 검색 요청을 하게 되는 경우
- time series 데이터(logs, metrics 등)

### 5. data_warm(w)

- time series 데이터를 유지 하고 있는 노드로 업데이트가 거의 없으며 드물게 요청 하는 경우

### 6. data_cold(c)

- time series 데이터를 유지 하고 있는 노드로 업데이트가 되지 않는 거의 요청을 하지 않는 데이터를 보유

### 7. data_frozen(f)

- time series 데이터로 요청도 업데이트로 없는 경우

### 8. ingest(i)

- 클러스터 내 적어도 하나 이상의 ingest 역할을 하는 노드 필요(ingest pipeline 기능을 사용하기 위해서 필요)
- master 와 data 노드와 같이 사용 하지 않는 것을 추천(ingesting시 부하가 걸리기때문에 분리하여 사용하는것을 추천)
- 색인 전에 데이터에 대한 변환하여 색인 되도록 함.

### 9. ml(l)

- ml 관련 기능(xpact 기본에서 사용불가)

### 10. remote_cluster_client(r)

- 원격으로 구성된 cluster에 연결 하여 원격 client 노드 역할을 수행

### 11. transform(t)

- 색인된 데이터로부터 데이터에 대한 pivot 이나 latest 정보를 별도 데이터로 변환해서 transform index로 저장

### 12. voting_only(v)

- 마스터 노드를 선출하기 위한 전용 노드
- 해당 노드로 사용하기 위해선 최소 master 노드 역할을 부여해야함
- node.roles: [master, voting_only]로 선언은 하며 마스터 노드의 역할은 수행.
- 마스터 노드로 선출은 되지 않음.(다른 역할을 부여할수도 있음.)

### etc. coordinating node(-)

- request, response만 해주는 노드. 데이터는 가지고 있지 않음.
- ex) search request 용, bulk indexing request용 등
- node.roles에 아무 역할을 적어주지 않은 경우.(node.roles: [])

---

## Components

### 1. Cluster

- cluster.name 설정이 가장 중요
- 기본 값은 elasticsearch
- cluster 구성 시 node 역할에 따른 구성 필수
- master node에 대한 quorum 구성 필수
  - quorum 구성이란 둘 이상의 클러스터 노드간 통신 실패시에 데이터 정합성을 유지하기 위해 각 노드로부터 투표를 진행하여 master 노드를 결정하는 구성
  
### 2. Node

- Elasticsearch 인스턴스가 시작될때 마다 실행
- 노드들의 모음이 Cluster
- 단일 노드로도 실행가능(=단일노드 클러스터)
- 설정기본: node.name과 node.roles
- **Master 노드**
  - 개별 노드와 인덱스에 대한 상태 관리와 메타 정보 관리를 담당
  - 특성에 맞춰 CPU, MEM에 대한 시스템 자원이 충분해야함.
- **Data 노드**
  - 색인한 문서의 shard가 저장되어 있는 노드
  - 문서에 대한 CRUD와 검색, 집계와 같은 데이터 작업 처리
  - Disk I/O, CPU, MEM 등에 대한 자원이 충분해야함.
- **Coordinating 노드**
  - 검색 요청이나 대량 색인 요청에 대한 라우팅 역할
  - 불필요한 요청을 master나 data 노드에서 처리할 필요가 없고 부하를 생성할 필요가 없기 때문
  - master노드와 유사하게 CPU, MEM에 대한 자원이 충분하면 좋음.

### 3. Index

- 분산된 Shard에 저장된 문서들의 논리적 집합
- 물리적으로는 Shard 하나가 하나의 독립된 Index로 동작하며, 루씬에서 보면 IndexWriter가 Shard당 하나씩 생성
- Primary shard와 Replica shard로 구성되며, Data Node에만 위치
- 데이터 유형에 따라 Hot, Warm, Cold, Frozen과 같이 분리해서 사용 가능
- ILM을 이용해서 용량에 따른 rolling 가능
- 루씬 기준의 Index를 Elasticsearch 에서는 Shard라고 함

### 4. Shard

- 물리적인 데이터가 저장되어 있는 단위
- Indexing 요청이 있을 때 분산된 노드에 위치한 shard 로 문서를 색인
- Index의 shard는 특정 node의 역할에 맞춰 배치 가능
- 이런 기능이 shard allocaition awareness 설정으로 적용이 가능하며, index setting 정보를 통해서 사용
- health status 정의는 shard의 상태를 가지고 정의내림
  - 녹색 : 모든 샤드가 정상적으로 할당되었을 때 상태
  - 노랑색 : Primary shard는 정상적으로 할당이 되었으나, replica shard 중 일부라도 할당이 되지 않았을 경우의 상태(서비스는 정상적으로 동작)
  - 빨강색 : Primary shard 중 하나 이상이 할당 되지 않았을 경우의 상태(서비스도 정상적으로 동작하지 않음)
- **Primary Shard**
  - 색인 요청이 들어오면 가장 먼저 생성해서 문서를 저장하게 되는 shard(=원본데이터)
  - 이를 기반으로 데이터를 복제하여 활용
  - 색인 성능을 개선하기 위한 포인트로 활용
  - Data 노드의 크기와 CPU 코어 크기를 고려해서 primary shard 크기를 설정
- **Replica Shard**
  - Primary shard를 기준으로 복제하는 shard
  - 검색 성능을 개선하기 위한 용도로 활용

---

## Setting

### Path settings

- path.data : 인덱스 데이터 저장 위치. array로 여러 저장소 사용가능
- path.logs : 로그 데이터 저장 위치.

### Cluster name setting

### Node name setting

### Network host settings

- network.host : 이 설정은 개발, 테스트 환경에서는 127.0.0.1 과 같은 루프백 주소만 바인딩 되지만 운영 환경에서는 일반적인 네트워크 설정으로 구성합니다.

### Discovery setting

- 운영환경으로 넘어갈때 중요한 설정
- discovery.seed_hosts : 클러스터링을 해야하는 노드리스트 등록
- cluster_inital_master_nodes : 마스터 노드 역할을 하는 노드들 등록

### jvm.options settings

- **Heap size settings**
  - System 리소스의 50%로 설정
  - 31GB 가 넘어가지 않도록 구성
  - 설정은 환경 변수로 set을 하거나 jvm.options 파일을 수정
  - ES_JAVA_OPTS="-Xms2g-Xmx2g"
- **JVM heap dump path setting**
  - Haep OutOfMemeory 에러 발생 시 heap dump 로그를 남기기 위한 경로 설정
  - 기본값 주로 사용. 수정은 자주 않함
  - GC logging settings
    - 기본 설정은 GC 옵션이 enable 되어 있음.
    - 기본 설정을 주로 사용.
  - Temporary directory settings
    - JVM에서 사용하기 위한 tmp 경로 설정
    - ES_TMPDIR환경 변수로 설정하거나 jvm.options에서 설정
    - 설정하지 않을 경우 Elasticsearch 내 TempDirectory 클래스를 이용해서 생성

### Cluster backups setting

장애 발생시 데이터 유실을 예방 하기 위한 설정으로 SLM(Snapshot Lifecycle Management)을 통해서 백업

### Circuit Breaker Settings (NodeScope)

- OutOfMemory 에러가 발생 하지 않도록 안정장치를 걸어 두는 것
- 검증된 설정값이 기본적으로 구성되어 있지만, 문제 발생시 설정 튜닝 필요
- **Parent circuit breaker**
  - 전체 heap size에 대한 total limit
  - `indices.breaker.total.use_real_memory(s)`
  - `indices.breaker.total.limit` : 위 설정이 false이면 70%로 설정되고, true이면 95%로 설정됨.
- **Field data circuit breaker**
  - field data cache(aggregation, sorting에 활용)를 사용 시 과도한 heap memory 사용 방지 목적
  - `indices.breaker.fielddata.limit` : 기본 JVM Heap size의 40%로 설정
  - `indices.breaker.fielddata.overhead`
    - 기본 40% 로 설정하지만, 실제 도달하면 heap memory가 부족할 수 있기 때문에 overhead 설정을 통해서 미리 차단
    - 기본 값은 1.03(fielddata 크기가 1이면 1.03으로 집계됨)
- **Request circuit breaker**
  - Aggregation 과 같은 요청에서 메모리 사용량 초과 방지
  - `indices.breaker.request.limit` : 기본 JVM Heap 크기의 60%로 설정
  - `indices.breaker.total.limit` : 기본 값 1

## Cluster-level shard allocation and routing settings

- shard를 노드에 어떻게 할당할 것인지에 대해 정의하는 설정
- recovery, replica allocation, rebalancing 등이 클러스터 내 노드가 추가/삭제 될 때 발생
- 마스터 노드는 이와 같이 클러스터를 운영/관리하기 위해 샤드들을 어떤 노드에 할당하고 이동시킬지를 결정
- 예) 클러스터에 대한 재시작 시 shard recovery와 rebalancing때문에 재시작이 되지 못하고 빈번하게 죽거나 재시작되는 현상이 발생함. 따라서, 재시작할때는 환경에 맞는 절차를 만들어 놓고 실행해야함
- shard allocation 중 exclude 설정
  - 기능, 장애가 발생시 문제 노드에 shard 할당되는 것 방지
  - 예) 특정 노드가 장애 발생했을 때, 해당 노드를 exclude시켜 신규 생성 인덱스에 대한 shard 할당 방지
  
    ```text
    PUT _cluster/settings
    {
      "transient": {
        "cluster.routing.allocation.exclude._ip":"장애발생노드IP"
      }
    }
    ```

- Cluster shard limit
  - 해당 설정을 통해 노드 별 shard 수를 제한하고 문제 발생 예방
  - `cluster.max_shards_per_node`
    - 기본 data 노드 당 1000개의 shard를 가질 수 있다.
    - Open 된 모든 shard를 포함한다.
- Shard allocation 설정은 4가지 형태
  1. cluster-level shard allocation settings
     - `cluster.routing.allocation.enable`
        - 노드가 재시작 될 때 local primary shard에 대한 recovery에 영향을 주지 않으며, 할당 되지 않은 replica shard에 대한 privmary shard를 즉시 recovery함.
        - all(기본설정) / primaries / new_privaries(신규 인덱스의 primary shard) / none
     - `cluster.routing.allocation.node_concurrent_incoming_recoveries`
     - `cluster.routing.allocation.node_concurrent_outgoing_recoveries`
     - `cluster.routing.allocation.node_concurrent_recoveries`  : 동시에 리커버리가 가능한 노드개수(incoming, outgoing 동시)
     - `cluster.routing.allocation.node_initial_primaries_recoveries`
     - `cluster.routing.allocation.same_shard.host` : 하나의 장비에 여러개의 elasticsearch 인스턴스를 구성할 때 같은 shard가 위치할수 있도록 설정함(기본 false는 같은 샤드로 배치 불가능)
     - 특정 노드에 인덱스의 샤드가 집중적으로 위치 하지 않도록 하여 균형을 이루게 하는 설정
       - `cluster.routing.rebalance.enable`
         - rebalace를 적용할 대상을 지정
         - all(기본) / primaries / replicas / none
       - `cluster.routing.allocation.allow_rebalance`
         - rebalance에 대한 동작을 허용할 대상을 지정
         - always / indices_primaries_active / indices_all_active(기본)
       - `cluster.routing.allocation.cluster_concurrent_rebalance` : 클러스터 기준으로 동시에 rebalancing 할 shard의 수를 설정(기본 2개). 너무 많은 경우 오버헤드 가능성도 있음.
  2. Disk-based shard allocation settings
     - 노드에 있는 disk의 용량에 따라 shard를 배치 시키는 설정
     - Elasticsearch의 경우 가장 많이 경험하는 오류가 disk full 에 따른 장애
     - elasticsearch 내 log 모니터링을해서 watermark 오류 에러나 경고 발생시 바로 대응 필요.
     - `cluster.routing.allocation.disk.threshold_enabled` : 기본 true이며, disk allocation decider를 사용
     - `cluster.routing.allocation.disk.watermark.low`
       - 기본 disk usage 85%로 구성
       - 85%가 되면 shard가 더이상 할당되지 않지만, 이 설정은 새로 만들어지는 primary shard에 적용되진 않고, replica shard에 대해서만 적용
       - usage가 아닌 남아 있는 여유공간 설정으로도 가능
     - `cluster.routing.allocation.disk.watermark.high`
       - 기본 disk usage 90% 이며, 초과 시 노드에 있는 샤드 재배치 시도
       - usage가 아닌 남아 있는 여유 공간 설정으로도 가능
     - `cluster.routing.allocation.disk.watermark.flood_stage`
       - 기본 95%로 설정 되어 있으며, disk usage가 설정을 넘은 노드가 있으면 읽기 전용으로 자동 전환되고 disk usage 가 떨어지게 되면 자동으로 해제
     - `cluster.info.update.interval` : 30초 간격으로 disk usage를 점검
  3. shard allocation awareness and Forced awareness
     - 노드 자체에 속성 설정을 해서 이용하는 방법
     - Elasticsearh는 shard를 할당할 때 물리적 하드웨어 구성 적용 가능
     - 같은 rack에 구성하거나 같은 zone에 구성되도록 지정 가능.
     - rack_id
       - node.attr.rack_id: rack_one
       - bin/elasticsearch -Enode.attr.rack_id=rack_one
     - attributes
       - cluster.routing.allocation.awareness.attributes: rack_id
         - 해당 설정을 해줘야 정상적으로 인식함.
       - master역할을 수행하는 모든 노드의 elasticsearh.yml에 정의하거나 cluster update settings를 이용해서 적용
     - force
       - 노드가 사용가능할때까지 replica shard의 할당이 되지 않도록 설정 가능
       - 강제로 할당한다고 생각하면됨.
       - cluster.routing.allocation.awareness.attributes: zone
       - cluster.routing.allocation.awareness.force.zone.values: zone1, zone2
     - 예제 코드

        ```text
        $ vi es1/config/elasticsearch.yml
        cluster.name: fastcampus-data-tier
        cluster.routing.allocation.awareness.attributes: tier
        node.name: data-hot
        node.roles: [ "master", "data" ]
        node.attr.tier: hot

        $ vi es2/config/elasticsearch.yml
        cluster.name: fastcampus-data-tier
        cluster.routing.allocation.awareness.attributes: tier
        node.name: data-cold
        node.roles: [ "master", "data" ]
        node.attr.tier: cold
        ```

        위처럼 정의한 2개의 elasticsearch node(hot, cold tier)를 실행한 상태에서 아래처럼 request하여 shard에 대한 배치를 변경진행.

        ```json
        PUT "http://localhost:9200/shard-allocation-00001"
        {
          "settings" : {
            "index.number_of_shards": 2,
            "index.number_of_replicas": 0,
            "index.routing.allocation.require.tier": "hot"
          }
        }
        ```

        위 PUT request시 shard 추가 완료됨. 관련 내용 조회하려면 "http://localhost:9200/_cat/shards/shard-allocation-00001?v" 에서 확인가능.

        ```json
        PUT "http://localhost:9200/shard-allocation-00001/_settings"
        {
          "index.routing.allocation.require.tier": "cold"
        }
        ```

        위 request까지 진행시에 shard가 data-hot에서 data-cold로 변경됨.

  4. Cluster-level shard allocation filtering

## Index Recovery Settings

- 이 설정은 샤드를 다시 생성하거나 재할당할 경우 primary shard 를 기준으로 복구하며, 개별 노드로의 in/out bound 크기의 총량으로 설정
- `indices.recovery.max_bytes_per_sec` : 기본 크기 40 MB/s

## Indexing buffer settings

- 이 설정은 색인 요청 문서를 in-memory로 담아서 빠르게 처리 하기 위해 사용
- memory buffer에 꽉 차면 segment 파일로 내려 씀
- 대량으로 색인 또는 빈번한 색인 요청이 많을 경우 색인 성능이 나오지 않을 때 살펴 보면 도움됨.
- 대부분의 색인 성능은 Disk I/O 영향을 많이 받음
- `indices.memory.index_buffer_size` : 기본 크기는 노드에 할당된 heap size의 10%이며 모든 샤드에서 buffer를 공유해서 사용

## Node query cache settings

- 질의 시 filter context를 이용해서 질의 결과를 cache 하도록 하는 설정
- 노드당 하나씩 존재하며, LRU 정책으로 사용
- cache 설정은 세그먼트 당 10000개의 문서 또는 heap size의 10%를 사용
- 세그먼크가 merge 되면 캐시된 결과가 유효하지 않음.
- Elasticsearch에서는 Field data cache도 제공
- fielddata circuit breaker 설정 영향을 받음
- 기본 field data cache 크기 설정은 무제한
- `indices.queries.cache.size` : 기본 head size의 10%

## Search settings

- 검색에 대한 전역 설정과 aggregation에 대한 제한을 구성하는 설정
- `indices.query.bool.max_clause_count`
  - 루씬 기준의 boolean query 절에 포함 될 수 있는 최대 절수
  - 기본 1024절
  - 설정이 너무 커지면 CPU, MEM에 대한 자원 소모 증가, 성능 저하
- `search.max_buckets` : 단일 응답에 허용되는 최대 aggregation bucket의 수(기본 65535개)
- `indices.query.bool.max_nested_depth` : bool query에서 사용되는 최대 nested 깊이를 정의(기본 20)

## Thread pools

- 기본 설정 수정하지 않으나, 단일 instance의 사양이 너무 좋아 elasticsearch를 여러개 실행시킬경우 processor의 크기를 나눠서 설정하는것을 추천
- `thread_pool.*`
- `node.processors`