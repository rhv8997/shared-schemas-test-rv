# CHANGELOG



## v1.7.6 (2024-04-08)

### Feature

* feat: adding evidence to boards

Adding `evidences` key to Boards ([`44720be`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/44720be5f01a08a76a304a2438bf02d41b5a30af))


## v1.7.5 (2024-04-03)

### Chore

* chore(release): 1.7.5 ([`646707f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/646707f484a2a745e46dd09cc2d82a92c9ce8d9d))

### Fix

* fix: check for model_fields before using ([`0299692`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0299692ace523791077bc0a0215e566248ad3dbf))


## v1.7.4 (2024-03-28)

### Chore

* chore(release): 1.7.4 ([`4054378`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/405437896deba717d456a52a04fb6ee215955be6))

### Feature

* feat: implement boards api

Create schema for boards. Note that this version of boards does not contain a version field.

ticket:https://www.notion.so/facultyai/Add-Boards-API-Table-b065910d97d54e6897ba227dcafec254?pvs=4 ([`990bc56`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/990bc56994fa33484a5b5e20146c3db577ee32eb))


## v1.7.3 (2024-03-27)

### Chore

* chore(release): 1.7.3 ([`b33adb4`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b33adb47003292cf3ab268e41075a180dd3708a5))

### Fix

* fix: check datetime type on serialise ([`f855666`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f85566645333c41c39a46d43a8cb73489fc9e45a))


## v1.7.2 (2024-03-26)

### Chore

* chore(release): 1.7.2 ([`a3d9da7`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a3d9da7b18381f879c8ffbd29674a3758ffc63a9))

### Unknown

* revert: restore signal/concept summaries ([`8ef7a96`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/8ef7a966edf87f56c733771fb359d3f1a0a3b833))


## v1.7.1 (2024-03-26)

### Chore

* chore(release): 1.7.1 ([`58ef3fb`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/58ef3fb3b3b45350e3014c15501620629158dc78))

### Style

* style: linting ([`7dbc840`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7dbc840830cadd2aa99235f10f003bc74876c964))


## v1.7.0 (2024-03-26)

### Chore

* chore(release): 1.7.0 ([`cbf6176`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/cbf617608e219823c772d811379e304d3ff51b87))

### Fix

* fix: partials must default to None ([`1302337`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1302337058608df2657b69cb6380fd0293ca1e07))


## v1.6.0 (2024-03-26)

### Chore

* chore(release): 1.6.0 ([`cecf3ce`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/cecf3cea0db8708291ed9fa03ddd5968647f01f6))

### Feature

* feat: evidence partial ([`2dfc64d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2dfc64d3820713e25a71e650c0256bbaad20dc2c))

### Fix

* fix: typo ([`aec030b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/aec030bf231ba74db894f785396707c4f39204a2))


## v1.5.0 (2024-03-26)

### Chore

* chore(release): 1.5.0 ([`4716ecd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4716ecda9bbe7497b3c3822966ea3a1ceb2af584))

### Feature

* feat: evidence refactor ([`16f1bdd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/16f1bdd3f022d71b152007bfe129c80f6ed03e14))


## v1.4.0 (2024-03-25)

### Breaking

* feat!: update evidence to have a separate label

changes evidence from being just links to links and labels, includes a new other_links field for non evidence links

existing values in evidence should be replaced with link entries with the same label and url ([`d01ffd7`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d01ffd73e21e9d392cadad0b0278645a44443a17))

### Chore

* chore(release): 1.4.0 ([`f03b7b6`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f03b7b61d052c2fcdccb074f6f79776613776115))

* chore(release): 1.3.0 ([`752f302`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/752f302ec8e3592375fd0659a94786e93a4b4be8))

* chore(release): 1.2.0 ([`385f8d5`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/385f8d51cc2bf6e2bc706e08bb79e2f565ffec22))

* chore(release): 1.1.0 ([`eb67eac`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/eb67eacb9832e251cb116ea9d2ca87dfc6974758))

* chore(release): 1.0.0 ([`837129f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/837129f8475f106843a164ae8fa53c8213657702))

### Ci

* ci: change step rules to prevent double runs on release ([`f3367bb`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f3367bb3bb84a5a8e41ac84e6c2af127efd88810))

* ci: temporarily disable git push during version ([`f184029`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f184029247d0f74785ac2aae85416d77a8a70f0f))

* ci: add missing push ([`441d24c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/441d24c8a4a02708344dc345d2e237d6c9cb72fe))

* ci: use common poetry ci image ([`ddc734d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/ddc734d208b7eeb7e95709c41572117bceef078b))

* ci: :construction_worker: add mr titile linter ([`3c25d8d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3c25d8d81348bc5d51065fc73f7cabd283c4ad81))

### Documentation

* docs: :memo: update readme for new pipeline ([`5ae2793`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/5ae2793cf1424cbf5b019d628098d56606f6b00b))

### Feature

* feat: update feeds

- List feeds returns feed summary rather than full feed.
- List feeds filters by archived.

Include how to migrate data in any modified or removed fields to new fields.

ticket: https://www.notion.so/facultyai/Implement-Feeds-API-v1-1-7cd293ac29414dc9aac9a9ebdfb8143f?pvs=4 ([`c2484d2`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c2484d2cd1fb3c96bb8b815c614549698a43e40e))

* feat: implement feeds api

Adding in feeds schema model

ticket: https://www.notion.so/facultyai/Implement-Feeds-API-7cd293ac29414dc9aac9a9ebdfb8143f?pvs=4 ([`199774f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/199774f2353f6d1df49d005e7d35cdeb2578144a))

* feat: add ip ref number and owner to signal and concept

Include IP reference number and IP owner in BaseSignal and CommonFields (Concept) classes.

ticket: https://www.notion.so/facultyai/Update-signal-and-concept-schema-to-support-IP-and-IP-owner-fields-726cc0aeccae4d44af1ed1c5052e4da0?pvs=4 ([`93040be`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/93040be86223eeb214f027bba74d661787a6ea1b))

* feat: add pilot ([`3407efd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3407efdd636eea0b92d3cae28b0156b6eb24af95))

### Fix

* fix: use str not httpurl for links ([`a2f4039`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a2f4039f12a4b6e91e7d256e12e78f5ab77923aa))


## v0.1.0 (2024-02-05)

### Build

* build: :arrow_up: pydantic v2 ([`2b3c547`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2b3c547d707bd2d9cbd574dc5e66fed2e48ca677))

### Chore

* chore(release): 0.1.0 ([`b9c2fc2`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b9c2fc2695d4348944d2b66ce3844a29dc4f1af8))

* chore: merge branch &#39;fix/revert-idf-number-change&#39; into &#39;master&#39;

fix: remove idf number

See merge request facultyai/defence/u108_build/u108_discovery_schemas!64 ([`7c87686`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7c87686b4d9a17aca2def659948462609ead03ac))

* chore: merge branch &#39;adp/idf-field&#39; into &#39;master&#39;

feat: idf number

See merge request facultyai/defence/u108_build/u108_discovery_schemas!62 ([`694771d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/694771d49b983e0f9593956f454034e0366b6f9e))

* chore: merge branch &#39;feature/owner-common-fields&#39; into &#39;master&#39;

feat: owner optional

See merge request facultyai/defence/u108_build/u108_discovery_schemas!61 ([`0d42ab3`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0d42ab3eb555da24e3475c236e4d92fde4ae593f))

* chore: merge branch &#39;feature/owner-update&#39; into &#39;master&#39;

feat: owner update

See merge request facultyai/defence/u108_build/u108_discovery_schemas!60 ([`2b3d340`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2b3d34004b6c27d62f6f69821bd9c037c5e30892))

* chore: merge branch &#39;feature/move-owner&#39; into &#39;master&#39;

feat: moved owner class

See merge request facultyai/defence/u108_build/u108_discovery_schemas!59 ([`8bc17ae`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/8bc17aeeb38235dec71183ce40cfc7c2195346f1))

* chore: merge branch &#39;feature/originator&#39; into &#39;master&#39;

feat: originator fields

See merge request facultyai/defence/u108_build/u108_discovery_schemas!58 ([`0112ac3`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0112ac3e1a8cf60a0d557dd950bec1010538f104))

* chore: merge branch &#39;feature/why-progressed&#39; into &#39;master&#39;

feat: why progressed

See merge request facultyai/defence/u108_build/u108_discovery_schemas!57 ([`16eedde`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/16eedde032d588c90320f5c53288cb10792ace7c))

* chore: merge branch &#39;feature/concept-why-interesting&#39; into &#39;master&#39;

feat: concept why interesting

See merge request facultyai/defence/u108_build/u108_discovery_schemas!56 ([`df4e322`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/df4e3226dd79a1fec464b168c9364e3472f47e00))

* chore: merge branch &#39;feature/rename-transition&#39; into &#39;master&#39;

feat: new fields and renaming

See merge request facultyai/defence/u108_build/u108_discovery_schemas!55 ([`2da1280`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2da1280e567c2e8840e6d8fcd1ff47ddf86ed3ba))

* chore: merge branch &#39;feat/update-stage-and-status-schema&#39; into &#39;master&#39;

feat: update state and status

See merge request facultyai/defence/u108_build/u108_discovery_schemas!54 ([`05cad89`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/05cad89c53e97147773a083f47df3dbc20c21713))

* chore: merge branch &#39;feature/how-long&#39; into &#39;master&#39;

feat: how long

See merge request facultyai/defence/u108_build/u108_discovery_schemas!53 ([`6bc1de1`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/6bc1de1bed868f4e214762373fb11b3bfd19355e))

* chore: merge branch &#39;feature/transition-fields&#39; into &#39;master&#39;

feat: transition fields

See merge request facultyai/defence/u108_build/u108_discovery_schemas!52 ([`18dc065`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/18dc06582f3408e07f55a9c5fbb7307154efc38e))

* chore: merge branch &#39;feat/use-decimal-in-place-of-float&#39; into &#39;master&#39;

fix: use Decimal in place of float

See merge request facultyai/defence/u108_build/u108_discovery_schemas!51 ([`eecab3c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/eecab3c27d5c43758a788fea7693f8c727336a6a))

* chore: merge branch &#39;feature/next-steps&#39; into &#39;master&#39;

feat: next steps class

See merge request facultyai/defence/u108_build/u108_discovery_schemas!50 ([`9b5006c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9b5006cf2e470f765b603f809348f1d5b8eca77a))

* chore: merge branch &#39;feature/current-position&#39; into &#39;master&#39;

feat: add current position field

See merge request facultyai/defence/u108_build/u108_discovery_schemas!48 ([`185df9c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/185df9c3dd7bd254b475a2723a9dfa1aec4ccad5))

* chore: merge branch &#39;fix/cone-of-plausability-correct&#39; into &#39;master&#39;

fix: correct type

See merge request facultyai/defence/u108_build/u108_discovery_schemas!47 ([`a499913`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a49991308e18f67908cc843872b075c28af41c22))

* chore: merge branch &#39;feature/cone-of-plausibility-field&#39; into &#39;master&#39;

feat: changed field name to cone of plausibility

See merge request facultyai/defence/u108_build/u108_discovery_schemas!46 ([`f854dfe`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f854dfe01608bb5a69a2dd91b4f3b4c4e80ed458))

* chore: merge branch &#39;fix/make-name-optional&#39; into &#39;master&#39;

fix: make name optional

See merge request facultyai/defence/u108_build/u108_discovery_schemas!45 ([`4ac69e2`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4ac69e2549742c729278d427ea86c17c00a079d5))

* chore: merge branch &#39;feat/add-shared-stage-to-base-stage&#39; into &#39;master&#39;

feat: adding a shared stage to the base stage taxonomy

See merge request facultyai/defence/u108_build/u108_discovery_schemas!42 ([`2d65e46`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2d65e46d715d282622defb7f01a26120a023b3a5))

* chore: merge branch &#39;jhlws/why-parked&#39; into &#39;master&#39;

fix: :label: add why-parked field

See merge request facultyai/defence/u108_build/u108_discovery_schemas!44 ([`9e4edfd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9e4edfd8113aaa6627881bd7ebb3bfcea0dbe7bb))

* chore: merge branch &#39;feature/legacy_fields_on_create&#39; into &#39;master&#39;

feat: :label: add legacy fields to create

See merge request facultyai/defence/u108_build/u108_discovery_schemas!43 ([`41d4a15`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/41d4a15044f73aec1a0c00eb00623ecb1fc22f71))

* chore: merge branch &#39;fix/fix-concept&#39; into &#39;master&#39;

Inherit from CommonFields

See merge request facultyai/defence/u108_build/u108_discovery_schemas!41 ([`b75d6fb`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b75d6fb608ff4289b2b02e3881bcdedb77c1bba1))

* chore: merge branch &#39;feature/add-why-parked&#39; into &#39;master&#39;

chore: add why parked

See merge request facultyai/defence/u108_build/u108_discovery_schemas!40 ([`c5ace50`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c5ace509f1d96f9ea3305ac6b43db927e30b9b9e))

* chore: add why parked ([`003e72b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/003e72b3da45e5c8e1990609e2ad42e1f1b8758e))

* chore: merge branch &#39;adp/revert-schema-name-change&#39; into &#39;master&#39;

fix: revert field name due to signal store dependency

See merge request facultyai/defence/u108_build/u108_discovery_schemas!39 ([`dc91df6`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/dc91df613f4d85a9622d592b4c34000f185d77bf))

* chore: merge branch &#39;adp/stage_update&#39; into &#39;master&#39;

feat: updated schemas for 2 layered stages

See merge request facultyai/defence/u108_build/u108_discovery_schemas!38 ([`998b31c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/998b31cb61a6b7f13ba478441954438940b85c1f))

* chore: merge branch &#39;fix/make-poc-fields-optional&#39; into &#39;master&#39;

fix: make role and email address optional on POC

See merge request facultyai/defence/u108_build/u108_discovery_schemas!37 ([`28c55cd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/28c55cd52ed69c2de013f0b24af80ae844b26289))

* chore: merge branch &#39;feature/assumption-refactor&#39; into &#39;master&#39;

fix: :bug: : vs =

See merge request facultyai/defence/u108_build/u108_discovery_schemas!36 ([`a8f1fe7`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a8f1fe7d61a492014744d2ac17c04f7cc75a83f1))

* chore: merge branch &#39;feature/assumption-refactor&#39; into &#39;master&#39;

fix: convert assumptions to list

See merge request facultyai/defence/u108_build/u108_discovery_schemas!35 ([`675ec91`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/675ec91bf4412ed0104eb7799d51d30dd7a5d1a0))

* chore: merge branch &#39;feature/s_t_fundementals&#39; into &#39;master&#39;

feat: :label: add s_t_fundamentals field to signals and concepts

See merge request facultyai/defence/u108_build/u108_discovery_schemas!34 ([`3c1ca8e`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3c1ca8e2ac6d48bb96e68bda64b8319f012ad7b2))

* chore: merge branch &#39;feautre/signal-taxonomies&#39; into &#39;master&#39;

fix: :label: change signal taxonomies to list of strings

See merge request facultyai/defence/u108_build/u108_discovery_schemas!33 ([`72d65f9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/72d65f9fa997aac9b93a7b1b3fbce33baf73dc3a))

* chore: merge branch &#39;feature/deeper-defaults&#39; into &#39;master&#39;

fix: default every field on concepts

See merge request facultyai/defence/u108_build/u108_discovery_schemas!32 ([`4c4b759`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4c4b75970c51be447b01e0921c7e18dfcad8f3e6))

* chore: refactor schema for nesting ([`9a406eb`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9a406ebe4e35905e12e7c5a9701c47157529b943))

* chore: add tagline ([`27e721f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/27e721f02a56bc5bac36e65a74bb6ef00c08374f))

### Ci

* ci: :green_heart: install semantic-release ([`80ae454`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/80ae454f99f6bd493ca459f13f8e8eac7c9ccefb))

* ci: :construction_worker: update to trunk style dev pattern ([`fc2290a`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/fc2290a35115b6889fde1791e53ce4b9a127acd4))

### Feature

* feat: updating base signal and concept to include archived ([`0752d28`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0752d2896dbb9d6c21f865b91baa6b02f48cf7e3))

* feat: add archived to comments ([`52d4a4c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/52d4a4cbb0ba1c7155187638fefa8a08519f5521))

* feat: add new fields ([`21daa75`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/21daa7526925ecaed3a5a0b451126e4f0059366e))

* feat: add comments, and history schemas ([`e616753`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e616753dc15452e9709fddd8dfff177b7fb59a98))

* feat: add archived flag ([`5e8b0ad`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/5e8b0adca4b7cb215c9c7585a97fba45ccb3e408))

* feat: correct summary types and spin off concepts ([`1a852b9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1a852b99b897f3e8c483af907d8ca58ea7097a25))

* feat: add status/stage fields ([`b9d5930`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b9d5930563eba00ae7cb0048ad367147cb99d06c))

* feat: update signal stage enum ([`7eae5bf`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7eae5bf3dce523f3bb6ce86b2e92973660d9dbcd))

* feat: Refactoring image schema ([`ec08d1e`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/ec08d1ea84ac678eaae0c18a675357916a72b1c6))

* feat: make system fields editable for admins ([`8915fab`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/8915fab4d433aec577ab19d2853114bf513cef7f))

* feat: concept why interesting ([`308a998`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/308a9988203d690de0449df24f81aa52e4ce54bf))

* feat: update state and status ([`fd09e6e`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/fd09e6e112321d9b053433deb4bf6625e93fcbe0))

* feat: add evidence_hub_ids to signal ([`a504d2f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a504d2f34cfff358cf96911231b48537a3dda8f0))

* feat(evidence): add link field ([`dc4d45e`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/dc4d45ee67ab13af02ce027cf1826684130e0959))

* feat: basic evidence schema ([`d6b2d69`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d6b2d697cad759821a5e7a6b60ceaf733c128508))

* feat: :label: add legacy fields to create ([`3f98dbc`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3f98dbc97b96aee10531df50793c4cc7c867cbc4))

* feat: :label: add s_t_fundamentals field to signals and concepts ([`9832b71`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9832b71872df1c279655695073e6bb2373a7867b))

* feat: poc type and give related a default value ([`aa58914`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/aa589140aac65f8235921acab7c35721651f7d13))

* feat: :truck: move signal_status and concept_status to status ([`aeb0792`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/aeb07927ecc34a7f6113290be8fab7a3271bccd7))

### Fix

* fix: hypothesis types ([`78a0642`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/78a0642443ed2f7c1e5744a7fe4e9e0639a9f4fd))

* fix: make how_found optional ([`1929c95`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1929c958e497472af9033eb1794cae13e229bf58))

* fix: expose edited field on comments ([`f358619`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f35861935ff933e6366a7106efdf36dc82597952))

* fix: coerce datetime schemas to integers ([`4e0ba53`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4e0ba5342bb95dfc147ec3b3d6a7ec3e9f7e68a9))

* fix: CreateComment fields are mandatory ([`90c400f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/90c400f3b888ca0a5a3e4fca89ee03bc764c80e4))

* fix: make new concept fields updatable ([`a9a2fdf`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a9a2fdf41bf9d50ada1ef7403006d4f2b275a24c))

* fix: match convention for priority enum ([`0173ded`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0173dedbbf459d3dfb4653c5b87d37edf53a7fe0))

* fix: use Decimal in place of float ([`68eebb3`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/68eebb3fcbf38725c830c22195b50c2dccfabd46))

* fix: evidence pydantic issue ([`e6466ec`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e6466ec47996f0b85fcabd80ceffaee3b45fd906))

* fix(evidence): date as datetime ([`4a65082`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4a650826de0a980ff527dadafd3da16043a0069d))

* fix: make name optional ([`be915fa`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/be915faedf391fd9d7ceb86006d7663503a5fe4f))

* fix: :label: add why-parked field ([`8580100`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/858010083c3de53205dad337cfa5af44a477e93d))

* fix: :bug: : vs = ([`6534c76`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/6534c764ec1b4894a27ffc09f63625fc75cfe123))

* fix: convert assumptions to list ([`ca4ed11`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/ca4ed110b2a6a9b15530379e5b06a7daabfde45b))

* fix: :label: change signal taxonomies to list of strings ([`7a8b4f5`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7a8b4f5d8c988137e2dcef8b8a676c2484d64318))

* fix: default every field on concepts ([`e4516cb`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e4516cb49f65723662a143953052fe8f9547c34c))

* fix: default all concept objects ([`2428ddc`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2428ddca6779d539f5f5a227c33d4cf71e0ca41f))

* fix: defaults in update objects ([`459287c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/459287ccfb0132fb5741f10766861d8cd5e133f4))

* fix: signalupdate should have no mandatory fields ([`f679524`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f6795246d4a3544a0e10ec1068ff975cc25c084c))

* fix: conceptupdate should have no mandatory fields ([`b28ca35`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b28ca35643cb6526310625b5a02433f8a68d8735))

* fix: make scores optional ([`89c848a`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/89c848a722418f989fc19e002c6d3a08067abf4f))

* fix: :bug: reorder enum creation ([`bf69f66`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/bf69f66ff4ee9a421cea6e9d04bc0411e619135f))

* fix: :bug: move status fields to stage ([`5fca97c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/5fca97cbf7925835dca2a0b8eae729bb1ad98f4f))

* fix: :bug: prevent stage nesting ([`a97a6dc`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a97a6dc541fc651a93c89ef243eb1b6e4c3a7cdc))

### Refactor

* refactor: :pencil2: fundamental vs fundemental ([`9897b26`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9897b26129656d3e797b683fd2f59b36787978fe))

* refactor: :art: move concept title etc to common fields ([`1c47207`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1c472075ae10407ed12f65a9237960b594cdea99))

* refactor: :technologist: use keyword arg for default ([`e38d303`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e38d3039d4a88ef79712958a58c82578effe9458))

* refactor: :technologist: default optional values ([`d4967fc`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d4967fc774f2b9aefa6cdfa698c5788fef41d389))

### Style

* style: :art: sort imports ([`178f960`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/178f960d8e90d45ce10ef10329e3ade439daf896))

### Unknown

* add triage signal stage ([`c3d1730`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c3d1730f7b38c1536d8e621e7ea017795c6d1e38))

* remove idf number ([`e323e7f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e323e7f491f9a37730ac2a0bd099fbd751080a5c))

* idf ([`b68d935`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b68d9352fb27503b28e3c5cde5d21583f30fe3da))

* owner optional ([`9a8d35d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9a8d35d2e31b417dbeee223ef0266c63d167e97a))

* owner update ([`cadaca4`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/cadaca4ed13c0b336de5bf4e6bf25f154374a32a))

* moved owner class ([`3e63485`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3e63485990200cec261d3232d095d196efb64691))

* signal owner move ([`3f9a812`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3f9a8126365ba86dbfc577a5d5a8aeaa81c60595))

* Move owner ([`76a6564`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/76a6564dd4081c938115b17b4ae5e88b90ea999f))

* originator fields ([`e8b79c8`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e8b79c8b6199c2318167508dcd449c4f418a115f))

* why progressed ([`21a9446`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/21a9446a7cf5b5e9ff1214fbf777cdbcdb028d59))

* new fields and renaming ([`51408e3`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/51408e3826179967ad9fbfe6fd6b262dc93f8fc5))

* decimal ([`f7ea586`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/f7ea586bd0a090240aae03157a09bd3bb468c01c))

* changed field name ([`00c51b9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/00c51b9bf396401617e3c6d4b032b028217e8037))

* transition fields ([`e95979c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e95979c9f326c645b9c79e420b176d050904ace7))

* next steps class ([`fd2b9dd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/fd2b9dd720c01c90ca59280bf5e32dd4c356758e))

* add current position field ([`b5dff4f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b5dff4f701add8729f32ab670668202b8195776f))

* correct type ([`7b3a772`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7b3a7725e5ce4c659707acc6d68f8a2883342d48))

* changed field name to cone of plausibility ([`8e5dde0`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/8e5dde0c404966bde0891d8d1b0d778563c7539c))

* added a shared stage ([`b2c5c1c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b2c5c1caedd4be51cc42a27ba4a9625cee9e344e))

* Inherit from CommonFields ([`7ae5809`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7ae58099d7f895428a0538da46775869224fae4c))

* Quick adjustment ([`af08bbc`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/af08bbc585cfcc4c948193d20393d38f4d7b67ce))

* Changing to substage ([`1565b5f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1565b5f9f71a9d1dcd89ebc757d79c0292cd19ce))

* Revert field name due to signal store dependency ([`4c14565`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4c145657eb7c95d2026ea7597856de612e2271fb))

* Make SignalUpdate inherit from SignalBase ([`b33a98b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b33a98b43fa10150b72055d21e7c6a81df5ecd9c))

* Updated schemas for 2 layered stages ([`e289eec`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e289eec8ed1c5e6025ad8d9f11d71ee8e6460056))

* Make role and email address optional on POC ([`834845f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/834845f93fd7b51be1fdea7ac3f5835eeae2982e))

* Merge branch &#39;feature/deep-defaults&#39; into &#39;master&#39;

fix: default all concept objects

See merge request facultyai/defence/u108_build/u108_discovery_schemas!31 ([`3e3d8c9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3e3d8c944d57598824078603c2d9ad8b17d0c953))

* Merge branch &#39;bugfix/optional-scores&#39; into &#39;master&#39;

fix: make scores optional

See merge request facultyai/defence/u108_build/u108_discovery_schemas!30 ([`710ac1d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/710ac1d3c0592c2c8910e9a6846b29df36d7b6f1))

* Merge branch &#39;feature/schema-refactor&#39; into &#39;master&#39;

chore: refactor schema for nesting

See merge request facultyai/defence/u108_build/u108_discovery_schemas!29 ([`bf1e369`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/bf1e369896213f41cb28ee6ed4b256e292077e0a))

* Merge branch &#39;feature/add-scores-to-concept&#39; into &#39;master&#39;

Add score to concept

See merge request facultyai/defence/u108_build/u108_discovery_schemas!28 ([`a5d1876`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a5d187629a83829e65d7aa75cbd163b7be551874))

* Add score to concept ([`1ac5d2b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1ac5d2b1045723624c8532936743218393096ff6))

* Merge branch &#39;feature/bump-pydantic&#39; into &#39;master&#39;

build: :arrow_up: pydantic v2

See merge request facultyai/defence/u108_build/u108_discovery_schemas!27 ([`0217757`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0217757a428ca48d7ce1083022fd9ba7edaffa75))

* Merge branch &#39;feature/add-dstf-effort-confidence-add-list-defaults&#39; into &#39;master&#39;

Add dstf_effort_confidence and list defaults

See merge request facultyai/defence/u108_build/u108_discovery_schemas!26 ([`ae52153`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/ae52153ae71f14603ac29aaf09bbe9fbfeff015c))

* Add dstf_effort_confidence and list defaults ([`01b5bf9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/01b5bf99c1eec732b3656a74a80aec038e50ce10))

* Merge branch &#39;feature/explicit-default-with-field&#39; into &#39;master&#39;

refactor: :technologist: use keyword arg for default

See merge request facultyai/defence/u108_build/u108_discovery_schemas!25 ([`a1b3eb3`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a1b3eb3d0fc369a64f3844422abe45fce8efeeae))

* Merge branch &#39;feature/default-values&#39; into &#39;master&#39;

refactor: :technologist: default optional values

See merge request facultyai/defence/u108_build/u108_discovery_schemas!24 ([`5b6a6ce`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/5b6a6ceb1e359acc675f9149dbbea09402e1d570))

* Make list fields optional on complete Signal and Concept ([`fbe4642`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/fbe4642d404183ea1a95dd04cb9aa8fe08c15784))

* Provide default values on complete signal ([`be2be2b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/be2be2bc7756024d0f953f0a40a44c8b3c6cfacf))

* Merge branch &#39;feat/add-poc&#39; into &#39;master&#39;

feat: poc type and give related a default value

See merge request facultyai/defence/u108_build/u108_discovery_schemas!23 ([`4244fef`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4244fefad2d08b5be60fa4d4e07bba0c5741bf76))

* Merge branch &#39;chore/add-taglne&#39; into &#39;master&#39;

chore: add tagline

See merge request facultyai/defence/u108_build/u108_discovery_schemas!22 ([`b66d68e`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b66d68e152c2e14091d87af56c4579a0d773e340))

* Merge branch &#39;stakeholder&#39; into &#39;master&#39;

fix: :label: sync figma and concept schema

See merge request facultyai/defence/u108_build/u108_discovery_schemas!21 ([`539b321`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/539b3217efdc33959de788888467e1538a88b392))

* sync figma and concept schema ([`1ea1ce4`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1ea1ce403b252e820030148eab45efdc6395a84e))

* Merge branch &#39;feature/make-summary-required&#39; into &#39;master&#39;

Make summary required

See merge request facultyai/defence/u108_build/u108_discovery_schemas!20 ([`6d9691e`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/6d9691ee40fa36b7dd29c4eb2c1a3d6cf4437e60))

* Make summary required ([`9fc5b48`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9fc5b48c697b4016e2be10cfe0289c26cd5b5c8c))

* cost to list ([`bd1e1c0`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/bd1e1c0ef9bb1552190bb4652e9686e36b24ab7b))

* change cost from list ([`5a79b91`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/5a79b919a00f147fe274a0b3b8fb4a948acc9b35))

* Merge branch &#39;fix/cost&#39; into &#39;master&#39;

change cost to decimal

See merge request facultyai/defence/u108_build/u108_discovery_schemas!18 ([`c3b4ba1`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c3b4ba1f1f772d7c30cd1a09147078ec49f76051))

* change cost to decimal ([`e6d28b0`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e6d28b088aeebcc4ad5d3c3fe0cbc4f7f3f2ec5f))

* Merge branch &#39;fix/status_update_to_stage&#39; into &#39;master&#39;

fix: :bug: move status fields to stage

See merge request facultyai/defence/u108_build/u108_discovery_schemas!17 ([`78b56bd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/78b56bdd3796cb1ca7166d845cfc2bd75164a32b))

* Merge branch &#39;feature/make-ref-id-final-entity-only&#39; into &#39;master&#39;

:label: Remove reference_id from create and update

See merge request facultyai/defence/u108_build/u108_discovery_schemas!16 ([`3f0c933`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3f0c933bd8a8858622f6cf5c95114b494ef38a61))

* :label: Remove reference_id from create and update ([`744b84b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/744b84b5945106474cb26ea17e1660630558f001))

* concepts ([`6e50641`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/6e50641abe3bad0ecd4ae7fe63dbc9424b0e738d))

* Merge branch &#39;refid/dashboard&#39; into &#39;master&#39;

add dashboard status to signals and reference_id to concepts

See merge request facultyai/defence/u108_build/u108_discovery_schemas!14 ([`175e642`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/175e6423242619cde6c9cde65f7ed25fd4a9e53e))

* additional attributes ([`d55466e`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d55466e2be4e805cf6d818012ddc8ec4aa013995))

* add related concepts attribute ([`27419d7`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/27419d72737268f5eef9be3f1e72dfbbb0ed7aa9))

* Merge branch &#39;master&#39; of https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas into refid/dashboard ([`a843ec9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a843ec9089396bc57266e959e35b270c91d3c898))

* Merge branch &#39;will/epoch-time&#39; into &#39;master&#39;

Change Modified Dates to Epoch Time

See merge request facultyai/defence/u108_build/u108_discovery_schemas!8 ([`045bbb6`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/045bbb6425d08ed5b8bab8b8ccfffb608b54d081))

* Change Modified Dates to Epoch Time ([`2ed95c6`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2ed95c6900b516407293539f249ecb948a1547d4))

* Merge branch &#39;feature/remove-max-length-constraint&#39; into &#39;master&#39;

Remove max length constraints

See merge request facultyai/defence/u108_build/u108_discovery_schemas!15 ([`9f4b022`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9f4b0226401ae47e860059528eae38a24a62c371))

* Remove max length constraints ([`a54b081`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a54b0811a8ba3d4aabe2fb5246bb8bcaa7fb8e2d))

* add dashboard status to signals and reference_id to concepts ([`c43ee67`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c43ee676857382b63e4e9c527c6efeb035836f43))

* Merge branch &#39;feature/update-validation-and-typo&#39; into &#39;master&#39;

Remove max chars

See merge request facultyai/defence/u108_build/u108_discovery_schemas!13 ([`4e628d0`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4e628d0ba477cfbc646cacca16573b748a79b123))

* Remove max chars ([`4ef5acd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4ef5acd28f84e901aa4511e2a0e23da0e5b0532d))

* Merge branch &#39;fix/status-enum&#39; into &#39;master&#39;

fix: :bug: prevent stage nesting

See merge request facultyai/defence/u108_build/u108_discovery_schemas!12 ([`ac1abf2`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/ac1abf26d88fefba75fb7d56d9b0c32d669e69d4))

* Merge branch &#39;shared-status-attribute&#39; into &#39;master&#39;

feat: :truck: move signal_status and concept_status to status

See merge request facultyai/defence/u108_build/u108_discovery_schemas!9 ([`4a8ab22`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4a8ab22748d31915ef182db6ce4f032757e9f521))

* Merge branch &#39;adp/update-documentation&#39; into &#39;master&#39;

Updated readme

See merge request facultyai/defence/u108_build/u108_discovery_schemas!11 ([`46eb66d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/46eb66dd68db8d47f7637dc0a18bbefe700343a6))

* Updated readme ([`3d53b2d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3d53b2d19b9d06ac586159f6954c5939e6c9b70c))

* Merge branch &#39;adp/stage-validation&#39; into &#39;master&#39;

Adding validation for the stages

See merge request facultyai/defence/u108_build/u108_discovery_schemas!10 ([`25d3287`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/25d328779375f572a4cc5396efd12564cd8f1ff2))

* add dstf effort reasoning ([`5a43ae9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/5a43ae92d7dd1c5c23368893ab32457efbb7a06c))

* Adding validation for the stages ([`41361c8`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/41361c8c615ddbd6f889a095968cc92cfed6f545))

* remove ref id from update ([`5d4fae5`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/5d4fae57196ce9936bb0415ba85e326d3a464d5c))

* add reference_id to signal alongside id ([`c6c546d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c6c546db71de4dd09a16f4b8a2475597b4dce729))

* typo in supporting documents field ([`a8a1302`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a8a13026ef7b99dee48a89f69f3b8b8317821e46))

* supporting evidence missing ([`6ee737f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/6ee737f004f1b32e4f7987b0aae71099e181652d))

* concepts schema update ([`bc0f048`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/bc0f04852b2936258dc337da820a2745cabddd49))

* create and update classes for concepts ([`76c31a2`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/76c31a2dd0d40531e416e76a221f37efc58ae014))

* typo in concept ([`4de4442`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/4de444205a383764df34beb24a3019f7981cde0e))

* Merge branch &#39;master&#39; of https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas ([`b367ea3`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b367ea3380655d3d9cbd847f7c64af870ed0d478))

* Revert score to int type ([`32d28f6`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/32d28f66e2fb357ac8b7e565ef66eb9417c93b60))

* str to int for score ([`d867ead`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d867eade9a457ffa4987054943323a1348416292))

* scores to str ([`097b2d9`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/097b2d9ce7dd2cff428f67e22aa1256179f8844d))

* change to reasoning from description ([`8751969`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/87519697b5577f7fcfd3d0b2f53f7b1a813887ac))

* remove score validation ([`8b9a3af`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/8b9a3af07822178c415117b3e590cd4a6c03b555))

* add confidence for TRUE ([`2361d85`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/2361d85bb620ce27646df09137efde654b929ca4))

* add none type to true score val ([`7927a89`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7927a896cf9e165956d15b01107bc3458cd0fd36))

* missing optionals ([`81e01ab`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/81e01ab973e282c8cfa23fe852b4d8714a2d9341))

* all but title and summary optional ([`17baf73`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/17baf73edf5818fc74a49fe68f9d6ca361d73990))

* : not = ([`539dc8f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/539dc8ff5ab6909150c5b3dc0ce7bd59daeddd07))

* remove trl from update ([`7e6718b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7e6718b78bc1092480a54452b029cac1d2623196))

* typo ([`dcdce8a`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/dcdce8a373c53f15683d1b1997ee485b8606fb41))

* Merge branch &#39;validation&#39; into &#39;master&#39;

change displayID name

See merge request facultyai/defence/u108_build/u108_discovery_schemas!7 ([`aa9be88`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/aa9be8857808c1ee0b88b44c63cb8e4f96ef9893))

* change displayID name ([`204d461`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/204d46111bc3af36af7d0db0c562139090cea728))

* Merge branch &#39;validation&#39; into &#39;master&#39;

schema updates

See merge request facultyai/defence/u108_build/u108_discovery_schemas!6 ([`c9435cc`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c9435cc1a1d291fe6d717133c5b581c845ddbe90))

* remove uneedned atts from update ([`0bc0e34`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0bc0e34e6b0daa27f60fcb7148117c1b30cfc130))

* change scores back to opt ([`71e87c4`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/71e87c43527ffea5642a4ac468f835ed33c4cccf))

* make disaply id optional for update ([`8b7823a`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/8b7823acc3042add17d9f453a262d0f76f317097))

* add display id ([`9b82b1f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/9b82b1f84916f1e05767f31b3f4c9f0a125dd6d6))

* schema updates ([`0597302`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0597302f5e91fbba5ed2412ff9906d805305cc01))

* Merge branch &#39;validation&#39; into &#39;master&#39;

make sup-ev optional on update

See merge request facultyai/defence/u108_build/u108_discovery_schemas!5 ([`b8df6c4`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b8df6c496cee75f380be89f3575cc63171d1b217))

* make sup-ev optional on update ([`7cc9150`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7cc91507f47082a4afe7d2d54eec928ca241877a))

* Remove supporting evidence validation ([`09201ba`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/09201ba3065c45a16aed3d1f490ef532ea36fd73))

* Merge branch &#39;validation&#39; into &#39;master&#39;

Validation

See merge request facultyai/defence/u108_build/u108_discovery_schemas!3 ([`317700c`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/317700ccad167ba3bd1ded041ee7ffef6a97d5a6))

* Merge branch &#39;validation&#39; of https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas into validation ([`a571719`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/a571719ed2793de85f90ad1fcd16d65bfea50cce))

* validation ([`20e94d7`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/20e94d70c495095a7bdec212564e24f9dbd552a9))

* Merge branch &#39;concepts&#39; into &#39;validation&#39;

add first draft concept schema

See merge request facultyai/defence/u108_build/u108_discovery_schemas!2 ([`d8f3ea5`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d8f3ea50d5bb1f1db26d80f1fc7a6e74fd7b30f7))

* add first draft concept schema ([`fef98f7`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/fef98f71fd3b652af1a843eb11eb9f10376f9065))

* added Field values and vlatidation ([`8b50a08`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/8b50a08e8454045ec8a211ba4df56d205f9e7868))

* Add common fields ([`d032110`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d032110a366700f6dfd7025147f2df4846e007fe))

* Add signal update ([`267947f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/267947fff557c3a969191eb680bfc694e8d57ef2))

* Match existing schema ([`0c31bf0`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/0c31bf08625be94a4f204bd00acedb01d10792ec))

* Make all optional ([`41853e1`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/41853e1c47a7c1ef7ed6460e85a0ad862b8a4593))

* Move pytyped ([`bfbab2b`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/bfbab2b17861a92ccdc1477eb921ac20d42de345))

* Update README ([`d7c462d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d7c462d34daeb484b6f100641168e47395791a06))

* Update README ([`b7025d3`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/b7025d3c391d05c204343770e8d0ac27b0164028))

* Use 0.0.0 in toml ([`31ceaa6`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/31ceaa66d6ec3563c5fdbc6210250d20d1a947ea))

* Use commit tag var ([`103e618`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/103e618718f244791b2ce7e4e3e5705fa6a9b4ab))

* Fetch tag with poetry ([`1f6f920`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1f6f920b45abad9ff9822068d1b142b467077035))

* Revert CI ([`bfcd175`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/bfcd175c1911e11c3d2e2e3d6f9dca6749931f2a))

* Add quotes ([`31675b8`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/31675b8614be105418256718e152abe1c29db997))

* Build on master ([`983e46d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/983e46d4c60b001335a9857b84887989fca70c26))

* echo version ([`1176e72`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/1176e725b30737c6ed26066f03bc9cb9fd4237e9))

* rename module directory ([`d7e2f40`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/d7e2f402a9c09c4fc037a91f0198d6c8dc723b0e))

* Update README ([`707f3cb`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/707f3cb7a837494b6603f016796cf99f5458a400))

* Run CI only on tags ([`e7e007f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/e7e007fcc35c980815ac6869778a5f0efdf79f73))

* Use correct dir name ([`c8a0b97`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/c8a0b97b44e0adbd968cee658ca76918eed49263))

* Update README ([`af4d1fd`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/af4d1fdddb34433950d2f12a6767dd4dd7943058))

* Add dynamic versioning ([`7c55b78`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/7c55b78833a835b811e4dbc845d885c372fa5fba))

* Add more config ([`96d472f`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/96d472fd61b2fc9990473dc50c7112f0e46ecac2))

* Add basic ci for shared schemas ([`3487a7d`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/3487a7df2dfbec04c5af158db1a3b0fbc4124008))

* Initial commit ([`33d5511`](https://gitlab.com/facultyai/defence/u108_build/u108_discovery_schemas/-/commit/33d55111cba162fc31442cdd18ce2dda083800e1))
